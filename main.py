import logging
from fastapi import FastAPI
from presentation.user_routes import router as user_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("log.txt"),     
        logging.StreamHandler()            
    ]
)

app = FastAPI()
app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Aplikasi FastAPI berjalan dengan sukses!"}
