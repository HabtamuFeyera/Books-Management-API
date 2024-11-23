from fastapi import FastAPI
from src.web import create_app

# Create the FastAPI app
app = create_app()

# Define a root route that returns a welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to the Books Management API!"}
