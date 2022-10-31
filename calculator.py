from tkinter import *
import math
from PIL import Image, ImageTk




root = Tk()
root.title("Calculator")

p1 = Image.open('logo.png')
photo=ImageTk.PhotoImage(p1)
root.wm_iconphoto(False,photo)

root.configure(background='white')


calc = Entry(root, width = 35, fg = "grey")
calc.grid(row = 0, column = 0, columnspan=4, padx=15, pady=10)

result = Entry(root, width = 15,)
result.grid(row = 0, column = 1, columnspan=4, padx=15, pady=10,)


def dotclick():
    current = result.get()
    result.delete(0, END)
    calc.delete(0, END)
    result.insert(0,str(current) + str("."))

def myclick(number):
    
    current = result.get()
    result.delete(0, END)
    calc.delete(0, END)
    result.insert(0,str(current) + str(number))

def clearing():
    result.delete(0, END)
    calc.delete(0, END)
    
def adding():
    firstnum = result.get()
    global fnum
    global calculate
    calculate = "plus"
    fnum = float(firstnum)
    result.delete(0, END)
    calc.delete(0, END)
    
def substracting():
    firstnum = result.get()
    global fnum
    global calculate
    calculate = "minus"
    fnum = float(firstnum)
    result.delete(0, END)
    calc.delete(0, END)
    
def multiplying():
    firstnum = result.get()
    global fnum
    global calculate
    calculate = "multiply"
    fnum = float(firstnum)
    result.delete(0, END)
    calc.delete(0, END)

def divididing():
    firstnum = result.get()
    global fnum
    global calculate
    calculate = "divide"
    fnum = float(firstnum)
    
    result.delete(0, END)
    calc.delete(0, END)


def sqrtc():
    firstnum = result.get()
    global fnum
    fnum = float(firstnum)
    result.delete(0, END)
    calc.delete(0, END)
    result.insert(0, fnum * fnum)
    calc.insert(0,str(fnum) + (" ") +   str("²") + (" ") +   str("="))    
    
def sqrtct():
    firstnum = result.get()
    global fnum
    fnum = float(firstnum)
    result.delete(0, END)
    calc.delete(0, END)
    result.insert(0, math.sqrt(fnum))
    calc.insert(0,str("√") + str(fnum) + (" ") +  str("="))    
 
def removing():

    result.delete(result.index("end")-1)


def equalres():
    secondnum = result.get()
    result.delete(0, END)
    global snum
    snum = float(secondnum)
    if calculate == "plus":
        result.insert(0, fnum + snum) 
        calc.insert(0,str(fnum) + (" ") +   str("+") + (" ") + str(snum) + (" ") +  str("="))
    elif calculate == "minus":
        result.insert(0, fnum - snum)
        calc.insert(0,str(fnum) + (" ") +  str("-") + (" ") +  str(snum)+ (" ") +  str("="))
    elif calculate == "multiply":
        result.insert(0, fnum * snum)
        calc.insert(0,str(fnum) + (" ") +   str("*") + (" ") +  str(snum)+ (" ") +  str("="))
    elif calculate == "divide":
        result.insert(0, fnum / snum)
        calc.insert(0,str(fnum) + (" ") +   str("/") + (" ") +  str(snum) + (" ") +  str("="))





#buttons

seven = Button(root, text="7",  command = lambda: myclick(7), padx=30, pady=30, fg="black",bg="white")   
eight = Button(root, text="8", command = lambda: myclick(8), padx=30, pady=30 , fg="black",bg="white")
nine = Button(root, text="9", command = lambda: myclick(9), padx=30, pady=30, fg="black",bg="white")  
four = Button(root, text="4", command = lambda: myclick(4), padx=30, pady=30, fg="black",bg="white")  
five = Button(root, text="5", command = lambda: myclick(5), padx=30, pady=30, fg="black",bg="white")  
six = Button(root, text="6", command = lambda: myclick(6), padx=30, pady=30, fg="black",bg="white")  
one = Button(root, text="1", command = lambda: myclick(1), padx=30, pady=30, fg="black",bg="white")  
two = Button(root, text="2", command = lambda: myclick(2), padx=30, pady=30, fg="black",bg="white")  
three = Button(root, text="3", command = lambda: myclick(3), padx=30, pady=30, fg="black",bg="white")  
add = Button(root, text="+", command = adding, padx=27.9, pady=30, fg="black",bg="white")  
subtract = Button(root, text="-", command =  substracting, padx=30, pady=30, fg="black",bg="white")  
multiply = Button(root, text="*", command = multiplying, padx=30, pady=30, fg="black",bg="white")  
zero = Button(root, text="0", command = lambda: myclick(0), padx=30, pady=30, fg="black",bg="white")   
equal = Button(root, text="=", command = equalres, padx=30, pady=30, fg="black",bg="white") 
dot = Button(root, text=".", command = dotclick,  padx=31.45, pady=30, fg="black",bg="white") 
divide = Button(root, text="/", command = divididing, padx=30, pady=30, fg="black",bg="white")
sqr =  Button(root, text="x²", command = sqrtc,  padx=30, pady=30, fg="black",bg="white")
sqrt = Button(root, text="√", command = sqrtct,  padx=30, pady=30, fg="black",bg="white")
remove =  Button(root, text="C", command = removing, padx=30, pady=30, fg="black",bg="white") 
clear = Button(root, text="R", command = clearing, padx=30, pady=30, fg="black",bg="white")  
#buttons on screen

sqrtc

seven.grid(row = 2, column = 0)
eight.grid(row = 2, column = 1)
nine.grid(row = 2, column = 2)
add.grid(row = 2, column = 3)

four.grid(row = 3, column = 0)
five.grid(row = 3, column = 1)
six.grid(row = 3, column = 2)
subtract.grid(row =3, column = 3)

one.grid(row = 4, column = 0)
two.grid(row = 4, column = 1)
three.grid(row = 4, column = 2)
multiply.grid(row = 4, column = 3)

zero.grid(row = 5, column = 0)
dot.grid(row=5, column = 1)
equal.grid(row= 5, column = 2) 
divide.grid(row= 5, column = 3)


sqr.grid(row=6, column = 0)
sqrt.grid(row=6, column = 1)
remove.grid(row=6, column = 2)
clear.grid(row= 6, column = 3)




root.mainloop()


