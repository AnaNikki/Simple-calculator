# Simple Calculator

## Description

This is a simple calculator program that performs basic arithmetic operations: addition, subtraction, multiplication, and division. It is written in Python, using the Tkinter library for the graphical user interface (GUI). 
The calculator allows the user to input two numbers and choose an operation to calculate the result.

### Features:
- Supports four basic operations: addition, subtraction, multiplication, and division.
- Handles invalid inputs and division by zero.
- Clear fields after calculation.

## Requirements
- Python 3.x
- Tkinter library (usually comes pre-installed with Python)

## Usage
1. When you run the Python script the calculator window will appear with the following components:

- Two number input fields to enter the numbers you want to perform calculations on.
- A dropdown or entry field to select the operation (addition, subtraction, multiplication, or division).
- A button to calculate the result.
- A label to display the result of the calculation.

2. Enter the first number, the second number, select the operation (e.g., +, -, *, /), and hit the calculate button. The result will be displayed on the screen.

4. If any invalid input is given, the program will show an error message prompting the user to input valid numbers.

## Code Overview
- `add(num1, num2)`: Returns the sum of the two numbers.
- `sub(num1, num2)`: Returns the difference between the two numbers.
- `mul(num1, num2)`: Returns the product of the two numbers.
- `div(num1, num2)`: Returns the quotient of the two numbers, or an error message if dividing by zero.
- `calculator()`: The main function to handle user input, perform the operation, and display the result.
- `clear_entries()`: Clears the input fields (first number, second number, and operation) after a calculation, preparing the calculator for a new operation.

## Error Handling
- Invalid input: If the user enters a non-numeric value, an error message will be displayed.
- Invalid operation: If the user enters an operation that is not supported, the program will notify them.
- Division by zero: If the user attempts to divide by zero, the program will handle the error gracefully and show the message "Division by Zero!".

## Screenshots
- Main calculator screen

![main - before calculation](https://github.com/user-attachments/assets/3f722584-3c4f-479d-974e-bbd56b6d7aaa)

- Result display

![main - after calculation](https://github.com/user-attachments/assets/39357596-872b-4f0c-84b9-7e0ba97c92a4)
