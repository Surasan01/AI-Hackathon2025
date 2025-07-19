from fastapi import FastAPI, HTTPException
import httpx
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

API2_URL = "http://api2:8001" 

@app.get("/")
async def forward_request():
    logging.info("API1 received request, forwarding to API2...")
    
    try:
        # ใช้ httpx เพื่อสร้าง client และยิง request ไปยัง API2
        async with httpx.AsyncClient() as client:
            response = await client.get(API2_URL)
            # if error
            response.raise_for_status() 
        
        logging.info(f"API1 received response from API2: {response.json()}")

        return response.json()

    except httpx.RequestError as e:
        logging.error(f"Could not connect to API2: {e}")
        raise HTTPException(status_code=503, detail="Service unavailable: Could not connect to API2.")
