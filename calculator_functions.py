import math  # Importing the math module for mathematical operations
import tkinter as tk  # Importing tkinter for GUI functionality
from tkinter import messagebox  # Importing messagebox to show error messages

# Function to evaluate the mathematical expression entered by the user
def calculate_expression(entry):
    try:
        expression = entry.get()  # Getting the expression from the entry widget
        expression = expression.replace('^', '**')  # Replacing '^' with '**' for exponentiation
        if 'sqrt' in expression:
            expression = expression.replace('sqrt', 'math.sqrt')  # Replacing 'sqrt' with math.sqrt function
        result = eval(expression, {"math": math, "__builtins__": {}})  # Evaluating the expression safely
        entry.delete(0, tk.END)  # Clearing the entry field
        entry.insert(tk.END, result)  # Displaying the result in the entry field
    except Exception:
        messagebox.showerror("Error", "Invalid Input")  # Showing error message if evaluation fails

# Function to clear the entry field
def clear_entry(entry):
    entry.delete(0, tk.END)  # Clearing all text from the entry field

# Function to perform trigonometric and logarithmic calculations
def perform_function(entry, func):
    try:
        value = float(entry.get())  # Converting input value to float
        if func == 'sin':
            result = math.sin(math.radians(value))  # Calculating sine value in degrees
        elif func == 'cos':
            result = math.cos(math.radians(value))  # Calculating cosine value in degrees
        elif func == 'tan':
            result = math.tan(math.radians(value))  # Calculating tangent value in degrees
        elif func == 'asin':
            result = math.degrees(math.asin(value))  # Calculating arcsine and converting to degrees
        elif func == 'acos':
            result = math.degrees(math.acos(value))  # Calculating arccosine and converting to degrees
        elif func == 'atan':
            result = math.degrees(math.atan(value))  # Calculating arctangent and converting to degrees
        elif func == 'log':
            result = math.log10(value)  # Calculating logarithm base 10
        elif func == 'ln':
            result = math.log(value)  # Calculating natural logarithm (base e)
        elif func == 'sqrt':
            result = math.sqrt(value)  # Calculating square root
        elif func == '^2':
            result = value ** 2  # Squaring the value
        
        entry.delete(0, tk.END)  # Clearing the entry field
        entry.insert(tk.END, result)  # Displaying the result in the entry field
    except Exception:
        messagebox.showerror("Error", "Invalid Input")  # Showing error message if conversion or calculation fails
