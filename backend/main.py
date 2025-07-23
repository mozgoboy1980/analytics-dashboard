from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import ga_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ga_routes.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "GA4 Dashboard backend is running"}
