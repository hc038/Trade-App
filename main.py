from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Database Configuration
DB_URL = "sqlite:///./trades.db"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Trade Order Model (Database Table)
class TradeOrder(Base):
    __tablename__ = "trade_orders"
    
    id = Column(Integer, primary_key=True, index=True)
    asset_symbol = Column(String, index=True)
    trade_price = Column(Float)
    trade_quantity = Column(Integer)
    trade_type = Column(String)

# Create database table
Base.metadata.create_all(bind=engine)

# FastAPI App Initialization
app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
# Pydantic Schema for Request Validation
class TradeOrderSchema(BaseModel):
    asset_symbol: str
    trade_price: float
    trade_quantity: int
    trade_type: str

# Database Dependency Injection
def get_db():
    db_session = SessionFactory()
    try:
        yield db_session
    finally:
        db_session.close()

# Endpoint to Create a New Trade Order
@app.post("/orders", response_model=TradeOrderSchema)
def submit_trade(trade_data: TradeOrderSchema, db: Session = Depends(get_db)):
    order_entry = TradeOrder(**trade_data.dict())
    db.add(order_entry)
    db.commit()
    db.refresh(order_entry)
    return order_entry

# Endpoint to Retrieve All Trade Orders
@app.get("/orders", response_model=list[TradeOrderSchema])
def fetch_all_trades(db: Session = Depends(get_db)):
    return db.query(TradeOrder).all()
