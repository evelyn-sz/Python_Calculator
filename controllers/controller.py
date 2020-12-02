from app import app
from calculator import *

@app.route('/')
def index():
    return "This is a basic calculator web app."

@app.route('/add/<var_1>/<var_2>')
def never_heard_of_calculator_add(var_1, var_2):
    return f"Result: {add(int(var_1), int(var_2))}"

@app.route('/subtract/<var_1>/<var_2>')
def never_heard_of_calculator_subtract(var_1, var_2):
    return f"Result: {subtract(int(var_1), int(var_2))}"

@app.route('/multiply/<var_1>/<var_2>')
def never_heard_of_calculator_multiply(var_1, var_2):
    return f"Result: {multiply(int(var_1), int(var_2))}"

@app.route('/divide/<var_1>/<var_2>')
def never_heard_of_calculator_divide(var_1, var_2):
    return f"Result: {divide(int(var_1), int(var_2))}"
