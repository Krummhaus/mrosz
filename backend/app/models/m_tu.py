from sqlmodel import SQLModel, Field
from typing import Optional

# Define the SQLModel for the existing table M_TU
class M_TU(SQLModel, table=True):
    # __table_name__ = "M_TU" #SQLAlchemy dunder
    __table_args__ = {"extend_existing": True}
    TU_CIS: str = Field(primary_key=True, max_length=4)  # Primary key
    FOLDER_PATH: Optional[str] = Field(default=None)  # Nullable TIMESTAMP
    POZN: Optional[str] = Field(default=None)  # Nullable TIMESTAMP
    ZALOZENO_UZIVATEL: Optional[str] = Field(default=None)  # Nullable TIMESTAMP
    ZALOZENO: Optional[str] = Field(default=None)  # Nullable TIMESTAMP
