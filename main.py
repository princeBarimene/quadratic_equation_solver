from tkinter import *
from math import sqrt

INPUT_WIDTH = 5


def quadratic_solver():
    a_value = float(a_input.get())
    b_value = float(b_input.get())
    c_value = float(c_input.get())

    sqrt_value = sqrt((b_value * b_value)-(4 * a_value * c_value))
    minus_b_value = (-1) * b_value
    two_a = 2 * a_value

    x1 = round((minus_b_value + sqrt_value)/two_a,2)
    x2 = round((minus_b_value - sqrt_value)/two_a,2) 
    x1_value_label.config(text = f"{x1}")
    x2_value_label.config(text = f"{x2}")

window = Tk()
# window.minsize(width=400, height=200)
window.title("Quadratic Equation Solver")
window.config(padx = 50, pady =25)


# creating labels
formular_label = Label(text=f"ax\u00B2 + bx + c", font=("Arial",30, "bold"), padx=10, pady=10)
formular_label.grid(column = 1, row = 0, columnspan=4)

a_label = Label(text="a = ")
a_label.grid(column=0, row=1)



b_label = Label(text="b = ")
b_label.grid(column=2, row=1)

c_label = Label(text="c = ")
c_label.grid(column=4, row=1)


root_label = Label(text="roots : ")
root_label.grid(column=0, row=3)

x1_label = Label(text=f"X\u2081 = ")
x1_label.grid(column=1, row=3)

x1_value_label = Label(text=0)
x1_value_label.grid(column=2, row=3)

x2_label = Label(text=f"X\u2082 = ")
x2_label.grid(column=4, row=3)

x2_value_label = Label(text=0)
x2_value_label.grid(column=5, row=3)




#creating button

calculate_button = Button(text="Calculate", command=quadratic_solver)
calculate_button.grid(column=2,row =2, columnspan= 2)


#creating input entries

a_input = Entry(width = INPUT_WIDTH)
a_input.grid(column=1, row=1)

b_input = Entry(width = INPUT_WIDTH)
b_input.grid(column=3, row=1)

c_input = Entry(width = INPUT_WIDTH)
c_input.grid(column=5, row=1)







window.mainloop()