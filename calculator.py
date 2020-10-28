from tkinter import *


root = Tk()
root.title('My Simple Calculator')

e = Entry(root, width=35, borderwidth=3)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# What will happen on different clicks
def on_click(num):
	current_num = e.get()
	e.delete(0, END)
	e.insert(0, str(current_num) + str(num))

def clear():
	e.delete(0, END)


# Math operations
def add():
	first_num = e.get()
	global f_num
	global math
	math = 'addition'

	f_num = int(first_num)
	e.delete(0, END)

def divide():
	first_num = e.get()
	global f_num
	global math
	math = 'division'

	f_num = int(first_num)
	e.delete(0, END)

def multiply():
	first_num = e.get()
	global f_num
	global math
	math = 'multiplication'

	f_num = int(first_num)
	e.delete(0, END)

def subtract():
	first_num = e.get()
	global f_num
	global math
	math = 'subtraction'

	f_num = int(first_num)
	e.delete(0, END)


#Get results
def equal():
	second_num = e.get()
	e.delete(0, END)

	if math == 'addition':
		e.insert(0, f_num + int(second_num))
	elif math == 'division':
		e.insert(0, f_num / int(second_num))
	elif math == 'multiplication':
		e.insert(0, f_num * int(second_num))
	elif math == 'subtraction':
		e.insert(0, f_num - int(second_num))




# Create buttons

number_1 = Button(root, text='1', padx=30, pady=20, command=lambda: on_click(1))
number_2 = Button(root, text='2', padx=30, pady=20, command=lambda: on_click(2))
number_3 = Button(root, text='3', padx=30, pady=20, command=lambda: on_click(3))

number_4 = Button(root, text='4', padx=30, pady=20, command=lambda: on_click(4))
number_5 = Button(root, text='5', padx=30, pady=20, command=lambda: on_click(5))
number_6 = Button(root, text='6', padx=30, pady=20, command=lambda: on_click(6))

number_7 = Button(root, text='7', padx=30, pady=20, command=lambda: on_click(7))
number_8 = Button(root, text='8', padx=30, pady=20, command=lambda: on_click(8))
number_9 = Button(root, text='9', padx=30, pady=20, command=lambda: on_click(9))

number_0 = Button(root, text='0', padx=30, pady=20, command=lambda: on_click(0))
button_clear = Button(root, text='C', padx=30, pady=20, command=clear)
button_equal = Button(root, text='=', padx=30, pady=20, command=equal)

button_add = Button(root, text='+', highlightbackground='#FFFAE5',padx=30, pady=20, command=add)
button_divide = Button(root, text='/', highlightbackground='#FFFAE5', padx=30, pady=20, command=divide)
button_multiply = Button(root, text='*', highlightbackground='#FFFAE5',padx=30, pady=20, command=multiply)
button_subtract = Button(root, text='-', highlightbackground='#FFFAE5',padx=30, pady=20, command=subtract)

# Display buttons
number_1.grid(row=3, column=0)
number_2.grid(row=3, column=1)
number_3.grid(row=3, column=2)

number_4.grid(row=2, column=0)
number_5.grid(row=2, column=1)
number_6.grid(row=2, column=2)

number_7.grid(row=1, column=0)
number_8.grid(row=1, column=1)
number_9.grid(row=1, column=2)

number_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_divide.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_add.grid(row=4, column=3)



# Plan:
# Create actions on clicks (add number to the input field)




root.mainloop()






















