from tkinter import *

INPUT_WIDTH = 5


def quadratic_solver():
    a_value = float(a_input.get())
    print(a_value)


window = Tk()
# window.minsize(width=400, height=200)
window.title("Quadratic Equation Solver")
window.config(padx = 50, pady =25)


# creating labels
a_label = Label(text="a = ")
a_label.grid(column=0, row=0)



b_label = Label(text="b = ")
b_label.grid(column=2, row=0)

c_label = Label(text="c = ")
c_label.grid(column=4, row=0)


root_label = Label(text="roots : ")
root_label.grid(column=0, row=2)

x1_label = Label(text=f"X\u2081 = ")
x1_label.grid(column=1, row=2)

x1_value_label = Label(text=0)
x1_value_label.grid(column=2, row=2)

x2_label = Label(text=f"X\u2082 = ")
x2_label.grid(column=4, row=2)

x1_value_label = Label(text=0)
x1_value_label.grid(column=5, row=2)




#creating button

calculate_button = Button(text="Calculate", command=quadratic_solver)
calculate_button.grid(column=2,row =1, columnspan= 2)


#creating input entries

a_input = Entry(width = INPUT_WIDTH)
a_input.grid(column=1, row=0)

b_input = Entry(width = INPUT_WIDTH)
b_input.grid(column=3, row=0)

c_input = Entry(width = INPUT_WIDTH)
c_input.grid(column=5, row=0)







window.mainloop()