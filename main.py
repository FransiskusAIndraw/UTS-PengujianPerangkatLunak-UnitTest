import logging
from fastapi import FastAPI
from presentation.user_routes import router as user_router

# Konfigurasi logging global
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("log.txt"),     # log disimpan ke file
        logging.StreamHandler()             # log juga muncul di terminal
    ]
)

app = FastAPI()
app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Aplikasi FastAPI berjalan dengan sukses!"}
