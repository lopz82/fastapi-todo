from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLITE_LOCAL = "sqlite:///./sql_app.db"
SQLITE_IN_MEMORY = "sqlite:///:memory:"
POSTGRES = "postgres://root:root@localhost:5432"

engine = create_engine(POSTGRES)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
