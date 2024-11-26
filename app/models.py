# from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Enum
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

# Create a class for all your database model classes to inherit from.
Base = declarative_base()


# Create a model for data table of users in postgres
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(Enum("male", "female", name="gender_enum"), nullable=False)
    age = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    activity_level = Column(Integer, nullable=False)
    user_created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()"))

class Tdee(Base):
    __tablename__ = "tdees"
    user_id = Column(Integer,ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True, nullable=False)
    tdee_number = Column(Integer, nullable=False)
    tdee_created_at = Column(TIMESTAMP(timezone=True), nullable=False,  primary_key=True, server_default=text("NOW()"))

class Bmi(Base):
    __tablename__ = "bmis"
    user_id = Column(Integer,ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True, nullable=False)
    bmi_number = Column(Integer, nullable=False)
    bmi_created_at = Column(TIMESTAMP(timezone=True), nullable=False,  primary_key=True, server_default=text("NOW()"))


class Food(Base):
    __tablename__ = "foods"
    food_name = Column(String, primary_key=True, nullable=False)
    food_calories = Column(Integer, nullable=False)
    food_created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()"))


class CaloriesConsumptions(Base):
    __tablename__ = "calories_consumptions"
    user_id = Column(Integer,ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True, nullable=False)
    eaten_food_name = Column(String, nullable=False)
    eaten_food_mass = Column(Integer, nullable=False)
    eaten_calories_number = Column(Integer, nullable=False)
    eaten_calories_created_at = Column(TIMESTAMP(timezone=True), nullable=False, primary_key=True, server_default=text("NOW()"))


class Exercises(Base):
    __tablename__ = "exercises_met"
    exercise_name = Column(String, nullable=False, primary_key=True)
    exercise_met = Column(Float, nullable=False)

class BurnedCalories(Base):
    __tablename__ = "burned calories"
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True, nullable=False)
    exercise_name = Column(String, nullable=False)
    exercise_met = Column(Float, nullable=False)
    exercise_time = Column(Float, nullable=False)
    burned_calories_number = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, primary_key=True, server_default=text("NOW()"))


class Total(Base):
    pass