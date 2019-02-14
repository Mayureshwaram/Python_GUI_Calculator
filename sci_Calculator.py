#***************************************************************************************************************
#                   This is a GUI calculator application using python
#***************************************************************************************************************

#==========================================Imported module======================================================
from tkinter import *
import math
import logging
import tkinter
#import tkinter.messagebox
from time import strftime
from datetime import datetime

#==========================================Logs formating=======================================================

filename = datetime.now().strftime("%a,%d %b %Y %H:%M:%S")  #The strftime() method returns a string representing 
                                                            #date and time using date, time or datetime object
logging.basicConfig(filename='log_'+filename +'.log',
                    format='%(levelname)s %(asctime)s :: %(message)s:%(lineno)d',
                    level=logging.DEBUG)

#==========================================Calculator Operations================================================
class Calculations():
    def __init__(this):
        this.total = 0
        this.current = ""
        this.new_num = True
        this.op_pending = False
        this.op = ""
        this.eq = False

        this.root = Tk()
        this.root.title("Calculators")

        this.root.configure(background="lightgrey")
        this.root.resizable(width=False , height=False)

        this.root.geometry("383x293")

        this.calc = Frame(this.root)
        this.calc.grid()
        
        this.txtDisplay1 = Entry(this.calc, font=('Times', 20 ,'bold'), bg="yellowgreen",\
                                 bd=8, width=35, justify = "right")
        this.txtDisplay1.grid(row=0 , column=0, columnspan=5)
        this.txtDisplay1.insert(0,"0")
        this.txtDisplay1.grid_remove()
      

        
        
        logging.debug("Inside of init fun: this.total=%s this.current=%s\
        this.new_num=%s this.op_pending=%s this.op=%s\t this.eq=%s @line no."
                      %(this.total,this.current,this.new_num,this.op_pending,
                      this.op,this.eq) )
        
    def num_press(this, num):
        this.eq = False
        temp = this.txtDisplay.get() or this.txtDisplay1.get()
        print("first num:",temp)
        temp2 = str(num)
        if this.new_num:
            this.current = temp2
            this.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            this.current = temp + temp2
        this.display(this.current)
        print("second num:",this.current)
        logging.debug("Inside of num press fun: %s is pressed @line.no" %this.current)

    def calc_total(this):
        this.eq = True
        this.current = float(this.current)
        if this.op_pending == True:
            this.do_cal()
        else:
            this.total = float(this.txtDisplay.get()) or float(this.txtDisplay1.get())

    def display(this, value):
        this.txtDisplay.delete(0, END) or this.txtDisplay1.delete(0, END)
        this.txtDisplay.insert(0, value)or this.txtDisplay1.insert(0, value)

    def do_cal(this):
        if this.op == "add":
            this.total += this.current
            logging.debug("Inside of addition operation, result is :%s @line no." %this.total)
        if this.op == "minus":
            this.total -= this.current
            logging.debug("Inside of subtraction operaton, result is :%s @line no." %this.total)
        if this.op == "mul":
            this.total *= this.current
            logging.debug("Inside of multiplication operaton, result is :%s @line no." %this.total)
        if this.op == "divide":
            this.total /= this.current
            logging.debug("Inside of division operaton, result is :%s @line no." %this.total)
        if this.op == "raise":
            print("current", this.current)
            print("total" ,this.total)
            this.total = this.total ** this.current

            #logging.debug("Inside of power to operaton result is:" %this.total)
        if this.op == "rootof":
            this.total = math.sqrt(this.current)
            logging.debug("Inside of square root operaton, result is :%s @line no." %this.total)
        if this.op == "fact":
            this.total=int(this.txtDisplay.get())or int(this.txtDisplay1.get())
            this.total=math.factorial(this.total)
            logging.debug("Inside of factorial operaton, result is :%s @line no." %this.total)
        if this.op == "log10":
            print(this.total)
            this.total=math.log10(this.current)
            #logging.debug("Inside of logarithmic operaton, result is :%s @line no." %this.total)
        if this.op == "sine":
            this.total=math.sin(math.radians(this.current))
            logging.debug("Inside of sine operaton, result is :%s @line no." %this.total)
        if this.op == "cosine":
            print(this.current)
            this.total = math.cos(math.radians(this.current))
            logging.debug("Inside of cosine operaton, result is :%s @line no." %this.total)
        if this.op == "tangent":
            this.total = math.tan(math.radians(this.current))
            logging.debug("Inside of tangent operaton, result is :%s @line no." %this.total)
        if this.op == "exp":
            this.total = math.exp(this.current)
            logging.debug("Inside of exponention operaton, result is :%s @line no." %this.total)

        this.new_num = True
        this.op_pending = False
        this.display(this.total)
        #logging.debug("Inside of do_cal fun, result is :%s @line no." %this.total)
        print("Inside of do_cal fun, result is :%s" %this.total)

    def operation(this, op):
        this.current = float(this.current)
        if this.op_pending:
            this.do_cal()
        elif not this.eq:
            this.total = this.current
        this.new_num = True
        this.op_pending = True
        this.op = op
        this.eq = False

    def clear(this):
        this.eq = False
        this.current = "0"
        this.display(0)
        this.new_num = True

    def all_clear(this):
        this.clear()
        this.total = 0

    def sign(this):
        this.eq = False
        this.current = -float(this.txtDisplay.get())or -float(this.txtDisplay1.get())
        this.display(this.current)

    def iExit(this):
        iExit = tkinter.messagebox.askyesno("Scientific Calculator","Confirm if you want to exit")
        if iExit > 0:
         root.destroy()
         return
    
    def Standard(this):
        this.txtDisplay1.grid_remove()
        this.root.resizable(width=False, height=False)
        this.root.geometry("383x293")
        return

    def Scientific(this):
        this.root.resizable(width=False, height=False)
        this.root.geometry("475x355")
        this.txtDisplay1 = Entry(this.calc, font=('Times', 20 ,'bold'), bg="yellowgreen",\
                                 bd=8, width=35, justify = "right")
        this.txtDisplay1.grid(row=0 , column=0, columnspan=5)
        this.txtDisplay1.insert(0,"0")
        return
    
    def about_cal(this):
        tkinter.messagebox.showinfo( "About Calculator","This is generalized calculator application.\
                                     \nCalculator Version :V1.0.0")
    def default_disp(this):
        this.txtDisplay = Entry(this.calc, font=('Times', 20 ,'bold'), bg="yellowgreen",\
                   bd=8, width=28, justify = "right")
        this.txtDisplay.grid(row=0 , column=0, columnspan=4, pady=1)
        this.txtDisplay.insert(0,"0")
        

CalObj = Calculations()
CalObj.default_disp()


#==========================================GUI Buttons=============================================

numbers = "789456123"               #sequence to be displayed on calculator gui
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(Button(CalObj.calc,height =2,width=6,padx=10, pady = 10, text = numbers[i]))
        bttn[i]["bg"]= "burlywood"
        bttn[i].grid(row = j, column = k,padx=1,pady=1)
        bttn[i]["command"] = lambda x = numbers[i]: CalObj.num_press(x)
        i += 1

bttn_0 = Button(CalObj.calc,height =2,width=6,padx=10, pady = 10, text = "0",bg="burlywood")
bttn_0["command"] = lambda: CalObj.num_press(0)
bttn_0.grid(row = 4, column = 0,  padx=1, pady = 1)

div = Button(CalObj.calc,height =2,width=6,padx=10, pady = 10, text = "/",bg="steel blue")
div["command"] = lambda: CalObj.operation("divide")
div.grid(row = 1, column = 3, padx=1, pady = 1)

mult = Button(CalObj.calc,height =2,width=6,padx=10, pady = 10, text = "*",bg="steel blue")
mult["command"] = lambda: CalObj.operation("mul")
mult.grid(row = 2, column = 3,  padx=1, pady = 1)

minus = Button(CalObj.calc,height =2,width=6,padx=10, pady = 10, text = "-",bg="steel blue")
minus["command"] = lambda: CalObj.operation("minus")
minus.grid(row = 3, column = 3, padx=1, pady = 1)

add = Button(CalObj.calc,height =2,width=6,padx=10, pady = 10, text = "+",bg="steel blue")
add["command"] = lambda: CalObj.operation("add")
add.grid(row = 4, column = 3,  padx=1, pady = 1)

power = Button(CalObj.calc, height=2,width=6,padx=10,pady=10,text="x^y",bg="sandybrown")
power["command"] = lambda: CalObj.operation("raise")
power.grid(row=2,column = 4,padx=1,pady=1)

fact = Button(CalObj.calc, height=2, width=6, padx=10, pady=10, text="!",bg="sandybrown")
fact["command"] = lambda: CalObj.operation("fact")
fact.grid(row=3,column=4, padx=1, pady=1)


log10 = Button(CalObj.calc, height=2, width=6, padx=10, pady=10, text="log10",bg="sandybrown")
log10["command"]= lambda: CalObj.operation("log10")
log10.grid(row=4, column=4, padx=1 , pady=1)

sine = Button(CalObj.calc, height=2,width=6, padx=10,pady=10, text = "sin" , bg= "sandybrown")
sine["command"]=lambda: CalObj.operation("sine")
sine.grid(row=5,column=0,padx=1,pady=1)

cosine = Button(CalObj.calc, height=2,width=6, padx=10,pady=10, text = "cos" , bg= "sandybrown")
cosine["command"]=lambda: CalObj.operation("cosine")
cosine.grid(row=5,column=1,padx=1,pady=1)

tangent = Button(CalObj.calc, height=2,width=6, padx=10,pady=10, text = "tan" , bg= "sandybrown")
tangent["command"]=lambda: CalObj.operation("tangent")
tangent.grid(row=5,column=2,padx=1,pady=1)

exponent = Button(CalObj.calc, height=2, width=6, padx=10, pady=10, text='e^x', bg="sandybrown")
exponent["command"]=lambda: CalObj.operation("exp")
exponent.grid(row=5,column=3,padx=1,pady=1)

rootof = Button(CalObj.calc, height=2, width=6, padx=10, pady=10, text="√", bg = "sandybrown")
rootof["command"] = lambda: CalObj.operation("rootof")
rootof.grid(row=5, column=4, padx=1, pady=1)

clear = Button(CalObj.calc,height =2,width=6,padx=10, pady = 10, text = "C",bg="coral")
clear["command"] = CalObj.all_clear
clear.grid(row = 4, column = 1, padx=1, pady = 1)

eq= Button(CalObj.calc,height =2,width=6,padx=10, pady = 10, text = "=",bg="palegreen")
eq["command"] = CalObj.calc_total
eq.grid(row = 4, column = 2,  padx=1, pady = 1)


point = Button(CalObj.calc,height =2,width=6,padx=10, pady = 10, text = ".",bg="sandybrown")
point["command"] = lambda: CalObj.num_press(".")
point.grid(row = 1, column = 4,  padx=1, pady = 1)

#==========================================GUI Menubar=============================================
   
menubar= Menu(CalObj.calc,background='skyblue')
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Standard", command = CalObj.Standard)
    

filemenu.add_command(label="Scientific", command = CalObj.Scientific)

filemenu.add_separator()
filemenu.add_command(label="Exit", command = CalObj.iExit)

help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About",command = CalObj.about_cal)

CalObj.root.config(menu=menubar)
CalObj.root.mainloop()

#=====================================================================================================
