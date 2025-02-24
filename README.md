Trade App is a simple backend service developed using Python 3.8 and the FastAPI framework. It allows users to submit and retrieve trade orders through REST APIs and manages trade data using an SQLite database. The service is containerized using Docker and deployed on an AWS EC2 instance with a fully automated CI/CD pipeline powered by GitHub Actions.

The API interacts with an SQLite database to store trade orders and provides easy access to trade data via two primary endpoints:

POST /orders – Submits new trade orders
GET /orders – Retrieves all submitted trade orders


Features
->Simple RESTful API for managing trade orders
->SQLite database integration using SQLAlchemy
->FastAPI automatic documentation with Swagger/OpenAPI
->Containerization with Docker and Docker Compose
->Continuous Integration/Deployment (CI/CD) using GitHub Actions
->Deployed on AWS EC2 for scalability


The API uses SQLite, a lightweight, file-based database system. Interactions with the database are handled using SQLAlchemy (an Object-Relational Mapping library for Python).

A table called trade_orders is automatically created to store order data.
Each entry in the table includes:
asset_symbol: Symbol of the traded asset (e.g., "AAPL" for Apple)
trade_price: Price at which the asset is traded
trade_quantity: Number of units bought or sold
trade_type: Type of trade order ("buy" or "sell")


API Endpoints

POST /orders
Request Body:
{
  "asset_symbol": "AAPL",
  "trade_price": 150.5,
  "trade_quantity": 10,
  "trade_type": "buy"
}
Response:
{
  "asset_symbol": "AAPL",
  "trade_price": 150.5,
  "trade_quantity": 10,
  "trade_type": "buy"
}

GET /orders
Response:
{
  "asset_symbol": "AAPL",
  "trade_price": 150.5,
  "trade_quantity": 10,
  "trade_type": "buy"
},
{
  "asset_symbol": "GOOGL",
  "trade_price": 2700.0,
  "trade_quantity": 5,
  "trade_type": "sell"
}



CI/CD Pipeline (GitHub Actions)
The GitHub Actions pipeline automates:

->Building the Docker image on commits
->SSH into the EC2 instance and deploys the latest build upon merging to main.


