from fastapi import FastAPI

# This creates your FastAPI application
app = FastAPI()

# This is your first API endpoint
@app.get("/")
def home():
    return {"message": "Welcome to ShopZen API", "status": "running"}

# Health check endpoint - every real company has this
@app.get("/health")
def health_check():
    return {"status": "healthy", "app": "ShopZen"}