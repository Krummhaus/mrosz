import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import m_tu

app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (use specific domains in production for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)
# Include M_TU router
app.include_router(m_tu.router, prefix="/M_TU", tags=["M_TU"])

# uvicorn main:app --host 0.0.0.0 --port 8000 --reload
