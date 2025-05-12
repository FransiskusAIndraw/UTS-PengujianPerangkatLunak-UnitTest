from fastapi import FastAPI
from presentation.user_routes import router as user_router

app = FastAPI()
app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Aplikasi FastAPI berjalan dengan sukses!"}

app.include_router(user_router)