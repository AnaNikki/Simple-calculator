import tkinter as tk
from tkinter import ttk


def add(num1, num2):
    result = num1 + num2
    return result


def sub(num1, num2):
    result = num1 - num2
    return result


def mul(num1, num2):
    result = num1 * num2
    return result


def div(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Division by Zero!"


def calculator():
    # Get input values from the user interface
    try:
        first_number = float(first_number_entry.get())  # Convert input to float for calculation
        second_number = float(second_number_entry.get())
        operator = operator_entry.get()

        # Perform the corresponding operation
        if operator == "+":
            result = add(first_number, second_number)
        elif operator == "-":
            result = sub(first_number, second_number)
        elif operator == "*":
            result = mul(first_number, second_number)
        elif operator == "/":
            result = div(first_number, second_number)
        else:
            result = "Invalid operation."

        # Update the result label
        calculate_label.config(text=str(result))

        # Clear input fields
        clear_entries()
    except ValueError:
        calculate_label.config(text="Invalid input. Please enter valid numbers.")


def clear_entries():
    first_number_entry.delete(0, tk.END)
    second_number_entry.delete(0, tk.END)
    operator_entry.delete(0, tk.END)


# Initialize the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("500x500")

# Create the main frame with padding
mainframe = ttk.Frame(window, padding=(5, 5, 5, 5))
mainframe.grid(column=0, row=0, sticky="NSEW")

# Allow window to expand properly
window.columnconfigure(0, weight=1, uniform="equal")  #  Allow mainframe to resize
window.rowconfigure(0, weight=1, uniform="equal")  #  Allow mainframe to resize

# Create a label for the first number input field
first_number_label = ttk.Label(mainframe, text="First number")
first_number_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

# Create an entry field for the user to input the first number
first_number_entry = ttk.Entry(mainframe, width=40)
first_number_entry.grid(row=0, column=1, padx=5, pady=5, sticky="EW")

# Create a label for the second number input field
second_number_label = ttk.Label(mainframe, text="Second number")
second_number_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")

# Create an entry field for the user to input the second number
second_number_entry = ttk.Entry(mainframe, width=40)
second_number_entry.grid(row=1, column=1, padx=5, pady=5, sticky="EW")

# Create a label for the operator input field (to specify the operation: +, -, *, /)
operator_label = ttk.Label(mainframe, text="Operator (+, -, *, /)")
operator_label.grid(row=2, column=0, padx=5, pady=5, sticky="W")

# Create an entry field for the user to input the operator
operator_entry = ttk.Entry(mainframe, width=40)
operator_entry.grid(row=2, column=1, padx=5, pady=5, sticky="EW")

# Create a label for displaying the result of the calculation
result_label = ttk.Label(mainframe, text="Result")
result_label.grid(row=3, column=0, padx=5, pady=5, sticky="W")

# Create a label for showing the calculated result (initialized as 0)
calculate_label = ttk.Label(mainframe, text="0", width=40)
calculate_label.grid(row=3, column=1, padx=5, pady=5, sticky="EW")

# Create a button that will trigger the calculation when clicked
calculate_button = tk.Button(mainframe, text="Calculate", command=calculator, width=10)
calculate_button.grid(row=3, column=2, padx=5, pady=5, sticky="EW")

# Set the focus on the first number entry field when the window is opened
first_number_entry.focus()

window.mainloop()
