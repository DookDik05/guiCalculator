import tkinter as tk

# Global declare the expression variable
expression = ""

# Create press function in the expression_field
def press(num):
    global expression
    expression = expression + str(num)
    # update expression
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""

def percent():
    try:
        global expression
        result = str(eval(expression + "/100"))
        equation.set(result)
        expression = result
    except:
        equation.set("error")
        expression = ""
        
def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)
    
def CE():
    global expression
    expression = expression[:-3]
    equation.set(expression)        

app = tk.Tk()

# Set Background color of GUI window
app.configure(background='gray')

# Set title
app.title("Simple Calculator")

# Set size of window
app.geometry("350x400")

equation = tk.StringVar()

# Create TextBox for expression
expression_field = tk.Entry(app, textvariable=equation, font=('Arial 20'), width=22, bd=5, insertwidth=4, bg="#a7a7a7", fg='#626164', justify='right')
expression_field.grid(columnspan=4)

# Create Button Number
btnpercent = tk.Button(app, text="%", bg="gray", fg='black', height=2, width=11, command=percent)
btnpercent.grid(row=2, column=0)

btnCE = tk.Button(app, text="CE", bg="gray", fg='black', height=2, width=11, command=CE)
btnCE.grid(row=2, column=1)

btnC = tk.Button(app, text="C", bg="gray", fg='black', height=2, width=11, command=clear)
btnC.grid(row=2, column=2)

btnrub = tk.Button(app, text=" <- ", bg="gray", fg='black', height=2, width=11, command=backspace)
btnrub.grid(row=2, column=3)

btn7 = tk.Button(app, text="7", bg="silver", fg='black', command=lambda: press(7), height=2, width=11)
btn7.grid(row=3, column=0)

btn8 = tk.Button(app, text="8", bg="silver", fg='black', command=lambda: press(8), height=2, width=11)
btn8.grid(row=3, column=1)

btn9 = tk.Button(app, text="9", bg="silver", fg='black', command=lambda: press(9), height=2, width=11)
btn9.grid(row=3, column=2)

btnx = tk.Button(app, text="x", bg="gray", fg='black', command=lambda: press("*"), height=2, width=11)
btnx.grid(row=3, column=3)

btn4 = tk.Button(app, text="4", bg="silver", fg='black', command=lambda: press(4), height=2, width=11)
btn4.grid(row=4, column=0)

btn5 = tk.Button(app, text="5", bg="silver", fg='black', command=lambda: press(5), height=2, width=11)
btn5.grid(row=4, column=1)

btn6 = tk.Button(app, text="6", bg="silver", fg='black', command=lambda: press(6), height=2, width=11)
btn6.grid(row=4, column=2)

btndelete = tk.Button(app, text="-", bg="gray", fg='black', command=lambda: press("-"), height=2, width=11)
btndelete.grid(row=4, column=3)

btn1 = tk.Button(app, text="1", bg="silver", fg='black', command=lambda: press(1), height=2, width=11)
btn1.grid(row=5, column=0)

btn2 = tk.Button(app, text="2", bg="silver", fg='black', command=lambda: press(2), height=2, width=11)
btn2.grid(row=5, column=1)

btn3 = tk.Button(app, text="3", bg="silver", fg='black', command=lambda: press(3), height=2, width=11)
btn3.grid(row=5, column=2)

btnplus = tk.Button(app, text="+", bg="gray", fg='black', command=lambda: press("+"), height=2, width=11)
btnplus.grid(row=5, column=3)

btn = tk.Button(app, text="/", bg="gray", fg='black', command=lambda: press("/"), height=2, width=11)
btn.grid(row=6, column=0)

btn0 = tk.Button(app, text="0", bg="silver", fg='black', command=lambda: press(0), height=2, width=11)
btn0.grid(row=6, column=1)

btndot = tk.Button(app, text=".", bg="gray", fg='black', command=lambda: press("."), height=2, width=11)
btndot.grid(row=6, column=2)

btnequal = tk.Button(app, text="=", bg="gray", fg='black', command=equalpress, height=2, width=11)
btnequal.grid(row=6, column=3)

app.mainloop()
