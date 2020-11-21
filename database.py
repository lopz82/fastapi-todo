from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLITE_LOCAL = "sqlite:///./sql_app.db"
SQLITE_IN_MEMORY = "sqlite:///:memory:"

engine = create_engine(SQLITE_LOCAL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
