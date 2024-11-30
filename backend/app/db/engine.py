from sqlmodel import create_engine

DATABASE_URL = "sqlite:///./db/mrosz_db.sqlite"
engine = create_engine(DATABASE_URL)
