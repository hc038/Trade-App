FROM python
MAINTAINER Hemchand
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install sqlalchemy
COPY ./main.py .
EXPOSE 8000
ENTRYPOINT ["python", "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]