from fastapi import FastAPI
import logging

# Terminal
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/")
def read_root():
    logging.info("API2 received a request.")
    return {"message": "Hello from API 2"}
