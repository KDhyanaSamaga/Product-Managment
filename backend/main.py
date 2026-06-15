from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, SessionLocal, get_db, engine
from modules.user.api import router as user_router

# Import all models here so SQLAlchemy knows about them before creating relationships
from modules.user.models import User
from modules.product.models import Product
from modules.bills.models import Bill, BillItem

app = FastAPI(title="Product Management API")

# Security: CORS Middleware
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173", # Vite default
    "http://localhost:8000",
    # Add your production frontend URL here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register routers
app.include_router(user_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Product Management API"}
