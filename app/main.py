from fastapi import FastAPI, HTTPException
from .operations import add, subtract, multiply, divide
from .logger import get_logger

app = FastAPI(title="FastAPI Calculator")
logger = get_logger()

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Calculator!"}

@app.get("/add")
def add_numbers(a: float, b: float):
    result = add(a, b)
    logger.info(f"Add {a} + {b} = {result}")
    return {"operation": "add", "a": a, "b": b, "result": result}

@app.get("/subtract")
def subtract_numbers(a: float, b: float):
    result = subtract(a, b)
    logger.info(f"Subtract {a} - {b} = {result}")
    return {"operation": "subtract", "a": a, "b": b, "result": result}

@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    result = multiply(a, b)
    logger.info(f"Multiply {a} * {b} = {result}")
    return {"operation": "multiply", "a": a, "b": b, "result": result}

@app.get("/divide")
def divide_numbers(a: float, b: float):
    try:
        result = divide(a, b)
        logger.info(f"Divide {a} / {b} = {result}")
        return {"operation": "divide", "a": a, "b": b, "result": result}
    except ValueError as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))

