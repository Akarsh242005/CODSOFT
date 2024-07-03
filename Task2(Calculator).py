from tkinter import *

window = Tk()
window.title("Arithmetic Calculator")
window.geometry("800x200")
window.configure(background='black')

def calculate_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
    except ValueError:
        result_label.config(text="Please enter valid numbers.")
        return
    operation = operation_var.get()
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result_label.config(text="Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        result_label.config(text="Please select an operation.")
        return
    result_label.config(text=f'Result: {result:.2f}')

def clear_fields():
    entry1.delete(0, END)
    entry2.delete(0, END)
    result_label.config(text="Result: ")
    operation_var.set("+")

label1 = Label(window, text="Number 1:", bg='lightblue')
label1.grid(row=0, column=0, padx=10, pady=5)

entry1 = Entry(window, bg='#ffffff')
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = Label(window, text="Number 2:", bg='lightblue')
label2.grid(row=1, column=0, padx=10, pady=5)

entry2 = Entry(window, bg='#ffffff')
entry2.grid(row=1, column=1, padx=10, pady=5)

operation_var = StringVar()
operation_var.set("+")

label3 = Label(window, text="Operation:", bg='#f0f0f0')
label3.grid(row=2, column=0, padx=10, pady=5)

operation_frame = Frame(window, bg='lightblue')
operation_frame.grid(row=2, column=1, padx=10, pady=5)

radio_add = Radiobutton(operation_frame, text="Add", variable=operation_var, value="+", bg='pink')
radio_add.pack(side=LEFT)

radio_subtract = Radiobutton(operation_frame, text="Subtract", variable=operation_var, value="-", bg='pink')
radio_subtract.pack(side=LEFT)

radio_multiply = Radiobutton(operation_frame, text="Multiply", variable=operation_var, value="*", bg='pink')
radio_multiply.pack(side=LEFT)

radio_divide = Radiobutton(operation_frame, text="Division", variable=operation_var, value="/", bg='pink')
radio_divide.pack(side=LEFT)

button_frame = Frame(window, bg='black')
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

submit_button = Button(button_frame, text="Calculate", command=calculate_sum, bg='#4CAF50', fg='black')
submit_button.pack(side=LEFT, padx=10)

clear_button = Button(button_frame, text="Clear", command=clear_fields, bg='#4CAF50', fg='black')
clear_button.pack(side=LEFT, padx=10)

result_label = Label(window, text="Result: ", bg='orange')
result_label.grid(row=4, column=0, columnspan=2, pady=5)

window.mainloop()
