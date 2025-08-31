# import libraries 

import tkinter as tk      # For GUI
import math               # To perform mathematical operations 
import re                 # regular expression for input validation

# Button click handler
def buttonClick(number):
    global operator
    if str(number) == ".":
        last_number = re.split(r'[\+\-\*/]', operator)[-1]
        if "." in last_number:
            return
        if operator == "" or operator[-1] in "+-*/":
            operator += "0"

    if operator == "" and str(number) in "+*/":
        return

    operator = operator +str(number)
    input_value.set(operator)

def buttonBackspace():   # backspace function to delete the last number from current input
     global operator
     operator=operator[:-1]
     input_value.set(operator)

def buttonClear():         # clear button function to clear current input
    global operator
    operator = ""
    input_value.set("")

def buttonEqual():          # equal button to evaluate expressions
    global operator
    try:      
            result =str(eval(operator))
            input_value.set(result)
            operator = result
    except ZeroDivisionError:
         input_value.set("Can not divide by Zero")
         operator=""
    except Exception:
          input_value.set("Invalid Expression")
          operator=""

def buttonSqrt():           # square root function for calculating square root of numbers
    global operator
    try:
        result = math.sqrt(eval(operator))
        input_value.set(str(result))
        operator = str(result)
    except ValueError:
        input_value.set("Invalid Input")
        operator = ""
    except:
        input_value.set("Error")
        operator = ""

# creating main application window
main =tk.Tk()              
main.title("My Calculator")          # title of the calculator window

operator = ""
input_value =tk.StringVar()

# display entry field
display_text = tk.Entry(main, font=("arial",20,"bold"),textvariable=input_value,bd=30,insertwidth=4,
                     bg="seashell",justify='right')

display_text.grid(columnspan=4,ipadx=8,ipady=25)

# creating buttons(numbers and operators)
# Row 1
btn_7 = tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="7",command=lambda: buttonClick(7))
btn_7.grid(row=1,column=0)

btn_8 = tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="8",command=lambda: buttonClick(8))
btn_8.grid(row=1,column=1)

btn_9 =tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="9",command=lambda: buttonClick(9))
btn_9.grid(row=1,column=2)

btn_add = tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="+",command=lambda: buttonClick("+"))
btn_add.grid(row=1,column=3)

# Row 2
btn_4 = tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="4",command=lambda: buttonClick(4))
btn_4.grid(row=2,column=0)

btn_5 =tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="5",command=lambda: buttonClick(5))
btn_5.grid(row=2,column=1)

btn_6 = tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="6",command=lambda: buttonClick(6))
btn_6.grid(row=2,column=2)

btn_sub = tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="-",command=lambda: buttonClick("-"))
btn_sub.grid(row=2,column=3)

# Row 3
btn_1 =tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="1",command=lambda: buttonClick(1))
btn_1.grid(row=3,column=0)

btn_2 =tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="2",command=lambda: buttonClick(2))
btn_2.grid(row=3,column=1)

btn_3 = tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="3",command=lambda: buttonClick(3))
btn_3.grid(row=3,column=2)

btn_multi = tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="*",command=lambda: buttonClick("*"))
btn_multi.grid(row=3,column=3)

# Row 4
btn_0 =tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="0",command=lambda: buttonClick(0))
btn_0.grid(row=4,column=0)

btn_decimal = tk.Button(main, padx=16, bd=8, fg="blue", font=("arial", 16, "bold"), text=".", command=lambda:buttonClick("."))
btn_decimal.grid(row=4, column=1)

btn_squareroot = tk.Button(main, padx=16, bd=8, fg="blue", font=("arial", 16, "bold"), text="√", command=buttonSqrt)
btn_squareroot.grid(row=4, column=2)

btn_div = tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="/",command=lambda: buttonClick("/"))
btn_div.grid(row=4,column=3)

# Row 5
btn_clear = tk.Button(main,padx=16,bd=8,fg="blue",font=("arial",16,"bold"),text="C",command=buttonClear)
btn_clear.grid(row=5,column=0)

btn_back = tk.Button(main, padx=16, bd=8, fg="blue", font=("arial", 16, "bold"), text="←", command=buttonBackspace)
btn_back.grid(row=5, column=1)

btn_equal =tk.Button(main,padx=16,pady=16,bd=8,fg="blue",font=("arial",16,"bold"),text="=",command=buttonEqual)
btn_equal.grid(row=5,column=2,columnspan=2,sticky='nsew',padx=5)

# Grid configuration for responsive layout
main.grid_rowconfigure(5, weight=1)
main.grid_columnconfigure(2, weight=1)
main.grid_columnconfigure(3, weight=1)

# Keyboard support for handling input by pressing keys on keyboard
def key_press(event):
    key = event.char
    if key in "0123456789.+-*/":
        buttonClick(key)
    elif key == "\r":  
        buttonEqual()
    elif key == "\x08":  
        buttonBackspace()

main.bind("<Key>", key_press)

main.mainloop()






