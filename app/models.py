import enum
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Enum
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

# Create a class for all your database model classes to inherit from.
Base = declarative_base()

# # Create a class for user attribute (gender)
# class GenderEnum(enum.Enum):
#     male = "Male"
#     female = "Female"


# Create a model for data table of users in postgres
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(Enum("male", "female",), nullable=False)
    age = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    user_created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()"))
