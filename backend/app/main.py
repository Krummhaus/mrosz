import uvicorn
import asyncio
import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional, List
from datetime import datetime


# Insance of FastAPI
app = FastAPI()


# Define the SQLModel for the existing table M_TU
class M_TU(SQLModel, table=True):
    # __table_name__ = "M_TU" #SQLAlchemy dunder
    __table_args__ = {"extend_existing": True}
    TU_CIS: str = Field(primary_key=True, max_length=4)  # Primary key
    FOLDER_PATH: Optional[str] = Field(default=None)  # Nullable TIMESTAMP
    POZN: Optional[str] = Field(default=None)  # Nullable TIMESTAMP
    ZALOZENO_UZIVATEL: Optional[str] = Field(default=None)  # Nullable TIMESTAMP
    ZALOZENO: Optional[str] = Field(default=None)  # Nullable TIMESTAMP


# Create the database engine
DATABASE_URL = "sqlite:///./db/mrosz_db.sqlite"
engine = create_engine(DATABASE_URL)

# seznam_tu = {"0411": Tu(tu_cis="0411", nazev_tu="Test 1")}


@app.get("/")
def read_root():
    return {"Hello": "World FastAPI"}


# Endpoint to retrieve an M_TU record by CIS_TU
@app.get("/M_TU/", response_model=List[M_TU])
@app.get("/M_TU/{TU_CIS}", response_model=M_TU)
def get_m_tu(TU_CIS: Optional[str] = None):
    with Session(engine) as session:
        if TU_CIS:
            # Query the database for a specific TU_CIS
            statement = select(M_TU).where(M_TU.TU_CIS == TU_CIS)
            result = session.exec(statement).first()

            if not result:
                raise HTTPException(status_code=404, detail="M_TU not found")

            # Convert the custom datetime format to a Python datetime object manually
            if result.ZALOZENO:
                try:
                    result.ZALOZENO = str(
                        datetime.strptime(result.ZALOZENO, "%Y%m%d%H%M%S.%f")
                    )
                except ValueError:
                    raise HTTPException(
                        status_code=500, detail="Error parsing datetime format"
                    )
            return result
        else:
            # Query the database for all records
            statement = select(M_TU)
            results = session.exec(statement).all()

            # Convert datetime for all records (if needed)
            for record in results:
                if record.ZALOZENO:
                    try:
                        record.ZALOZENO = str(
                            datetime.strptime(record.ZALOZENO, "%Y%m%d%H%M%S.%f")
                        )
                    except ValueError:
                        raise HTTPException(
                            status_code=500, detail="Error parsing datetime format"
                        )
            return results


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
