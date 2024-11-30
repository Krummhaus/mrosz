import uvicorn
from fastapi import FastAPI
from routers import m_tu

app = FastAPI()

# Include M_TU router
app.include_router(m_tu.router, prefix="/M_TU", tags=["M_TU"])

@app.get("/")
def read_root():
    return {"Hello": "World FastAPI"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
