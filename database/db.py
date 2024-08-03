from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
import psycopg2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Database:

    async def get_db():
        url = "postgresql+psycopg2://aaditya:{password}@localhost:5432/inventory_management"
        engine = create_engine(url)
        Base.metadata.create_all(engine)
        print("tables created successfully!")
        session = sessionmaker(bind = engine)

        if not database_exists(engine.url):
            create_database(engine.url)
            print("Creating Database inventory_management")

        return session
        

        
