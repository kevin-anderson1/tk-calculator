import tkinter as tk

curr_display = '       '
window = tk.Tk()
window.title('Calculator')
window.geometry('130x180')
header = tk.Label(window, text='Calculator')
header.grid(row=1, column=6, columnspan=3)
display = tk.Label(window, text=curr_display)
display.grid(row=3, column=5, columnspan=3)


numbers = []
for i in range(1,10):
    button = tk.Button(window, text=i, state=tk.NORMAL, command=lambda i=i: num_in(i))
    numbers.append(button)
    
zero_btn = tk.Button(window, text='0', state=tk.NORMAL, command=lambda i=0: num_in(i))
zero_btn.grid(row=8, column=6)

    
for row in range(0,3):
    for column in range(0,3):
        i = row * 3 + column
        numbers[i].grid(row=row+5, column=column+5,)
             
def num_in(i):
    global curr_display
    curr_display = curr_display + str(i)
    display = tk.Label(window, text=curr_display, padx=10)
    display.grid(row=3, column=5, columnspan=3)

def addition():
    global num1, curr_display, operation
    num1 = int(curr_display)
    curr_display = '           '
    display = tk.Label(window, text=curr_display, padx=10)
    display.grid(row=3, column=5, columnspan=5)
    operation = 'add'
    
def subtraction():
    global num1, curr_display, operation
    num1 = int(curr_display)
    curr_display = '       '
    display = tk.Label(window, text=curr_display, padx=10)
    display.grid(row=3, column=5, columnspan=5)
    operation = 'subtract'
    
def divide():
    global num1, curr_display, operation
    num1 = int(curr_display)
    curr_display = '        '
    display = tk.Label(window, text=curr_display, padx=10)
    display.grid(row=3, column=5, columnspan=5)
    operation = 'divide'
    
def multiply():
    global num1, curr_display, operation
    num1 = int(curr_display)
    curr_display = '          '
    display = tk.Label(window, text=curr_display, padx=10)
    display.grid(row=3, column=5, columnspan=5)
    operation = 'multiply'
    
def equal():
    global num2, curr_display, operation
    num2 = int(curr_display)
    
    if operation =='add':
        curr_display = str(num1 + num2)
    
    elif operation == 'subtract':
        curr_display = str(num1 - num2)
        
    elif operation == 'divide':
        try:
            curr_display = str(num1/num2)
        except ZeroDivisionError:
            curr_display = 'Error'
    
    elif operation == 'multiply':
        curr_display = str(num1*num2)
        
    display = tk.Label(window, text=curr_display, padx=10)
    display.grid(row=3, column=5, columnspan=5)
    
def clear():
    global num1, num2, curr_display, opertaion
    num1 = None
    num2 = None
    curr_display = '         '
    operations = None
    display = tk.Label(window, text=curr_display, padx=10)
    display.grid(row=3, column=5, columnspan=5)
    
    
add_btn = tk.Button(window, text='+', command=lambda : addition())
add_btn.grid(row=5, column=10)

subtract_btn = tk.Button(window, text='-', command=lambda : subtraction())
subtract_btn.grid(row=6, column=10)

divide_btn = tk.Button(window, text='/', command=lambda : divide())
divide_btn.grid(row=7, column=10)

multiply_btn = tk.Button(window, text='x', command=lambda : multiply())
multiply_btn.grid(row=8, column=10)

equal_btn = tk.Button(window, text='=', command=lambda: equal())
equal_btn.grid(row=9, column=10)

clear_btn = tk.Button(window, text='Clear', command=lambda: clear())
clear_btn.grid(row=11, column = 6)

        
window.mainloop()
