from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime

# Database setup
DATABASE_URL = "sqlite:///weather_stat.db"
engine = create_engine(DATABASE_URL, echo=True)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Define Base
Base = declarative_base()

# Location Model
class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    weather_records = relationship('WeatherRecord', back_populates='location', cascade='all, delete-orphan')

    def __repr__(self):
        return f"Location(id={self.id}, city='{self.city}', country='{self.country}')"

    @classmethod
    def add_location(cls, city, country):
        location = cls(city=city, country=country)
        session.add(location)
        session.commit()
        return location

    @classmethod
    def get_all_locations(cls):
        return session.query(cls).all()

    @classmethod
    def find_location_by_id(cls, location_id):
        return session.query(cls).filter_by(id=location_id).first()

    @classmethod
    def delete_location(cls, location_id):
        location = cls.find_location_by_id(location_id)
        if location:
            session.delete(location)
            session.commit()
            return True
        return False

# Weather Record Model
class WeatherRecord(Base):
    __tablename__ = 'weather_records'
    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('locations.id'))
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    wind_speed = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    location = relationship('Location', back_populates='weather_records')

    def __repr__(self):
        return f"WeatherRecord(id={self.id}, location_id={self.location_id}, temperature={self.temperature}, humidity={self.humidity}, wind_speed={self.wind_speed}, date={self.date})"

    @classmethod
    def add_weather_record(cls, location_id, temperature, humidity, wind_speed):
        weather_record = cls(
            location_id=location_id,
            temperature=temperature,
            humidity=humidity,
            wind_speed=wind_speed
        )
        session.add(weather_record)
        session.commit()
        return weather_record

    @classmethod
    def get_all_weather_records(cls):
        return session.query(cls).all()

    @classmethod
    def find_weather_by_id(cls, record_id):
        return session.query(cls).filter_by(id=record_id).first()

    @classmethod
    def delete_weather_record(cls, record_id):
        weather_record = cls.find_weather_by_id(record_id)
        if weather_record:
            session.delete(weather_record)
            session.commit()
            return True
        return False

# Create database tables
Base.metadata.create_all(engine)

# Add sample data if running as main script
if __name__ == "__main__":
    print("Creating tables and inserting sample data...")
    
    # Add sample locations
    location1 = Location.add_location(city="Nairobi", country="Kenya")
    location2 = Location.add_location(city="New York", country="USA")
    location3 = Location.add_location(city="Tokyo", country="Japan")
    
    print(f"Added Locations: {location1}, {location2}, {location3}")

    # Add sample weather records
    if location1:
        WeatherRecord.add_weather_record(location_id=location1.id, temperature=25.5, humidity=60.0, wind_speed=12.3)
    if location2:
        WeatherRecord.add_weather_record(location_id=location2.id, temperature=18.2, humidity=55.5, wind_speed=8.7)
    if location3:
        WeatherRecord.add_weather_record(location_id=location3.id, temperature=22.1, humidity=70.0, wind_speed=10.2)
    
    print("Sample data added successfully!")
