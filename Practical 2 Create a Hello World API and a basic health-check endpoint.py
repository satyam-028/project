from fastapi import FastAPI

app = FastAPI()


# Hello World API
@app.get("/")
def hello():
    return {"message": "Hello World"}


# Health Check API
@app.get("/health")
def health_check():
    return {"status": "healthy"}