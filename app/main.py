from fastapi import FastAPI
from app.routers import user, tdee, bmi, food, calories_consumption, exercises, burned_calories

# Create an instance of the FastAPI class, which represents a web application.
app = FastAPI()

#  Create a set of routes (defined in a separate router module or class) into the main FastAPI application (app)
app.include_router(user.router)
app.include_router(tdee.router)
app.include_router(bmi.router)
app.include_router(food.router)
app.include_router(calories_consumption.router)
app.include_router(exercises.router)
app.include_router(burned_calories.router)


@app.get("/")
async def root():
    return  {"data": "hello"}