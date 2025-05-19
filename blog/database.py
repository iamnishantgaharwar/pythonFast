from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'postgresql://neondb_owner:7oGuihjlS6sD@ep-dawn-haze-a1s136dd-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require'


engine = create_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()