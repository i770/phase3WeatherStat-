from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database Connection
DATABASE_URL = "sqlite:///weather_stat.db"
engine = create_engine(DATABASE_URL, echo=True)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
