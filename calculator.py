from tkinter import *
def btnClick(numbers):
    global operator
    operator = operator +str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup= str(eval(operator))
    text_Input.set(sumup)
    operator=""
cal = Tk()
cal.title("Calculator")
cal.minsize(width=400, height=500)
cal.maxsize(width=400, height=500)
operator=""
text_Input= StringVar()
entry = Entry(cal, font=('arial' , 20, 'bold'), textvariable= text_Input,
              bd= 30, bg= "powder blue", justify= 'right')
button7= Button(cal, text= "7", padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold'),
                bg= 'powder blue' , justify= 'right', command= lambda : btnClick(7))
button8= Button(cal, text= "8", padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold')
                , bg= 'powder blue' , justify= 'right', command= lambda : btnClick(8))
button9= Button(cal, text= "9", padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold')
                , bg= 'powder blue' , justify= 'right', command= lambda : btnClick(9))
add= Button(cal, text= "+", padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold'),
            bg= 'powder blue' , justify= 'right', command= lambda : btnClick("+"))

button4= Button(cal, text= "4", padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold')
                , bg= 'powder blue' , justify= 'right', command= lambda : btnClick(4))
button5= Button(cal, text= "5", padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold'),
                bg= 'powder blue' , justify= 'right', command= lambda : btnClick(5))
button6= Button(cal, text= "6", padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold'),
                bg= 'powder blue' , justify= 'right', command= lambda : btnClick(6))
subtract= Button(cal, text= "-", padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold'),
                 bg= 'powder blue' , justify= 'right', command= lambda : btnClick("-"))

button1= Button(cal, text= '1', padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold'),
                bg= 'powder blue' , justify= 'right', command= lambda : btnClick(1))
button2= Button(cal, text= "2", padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold'),
                bg= 'powder blue' , justify= 'right', command= lambda : btnClick(2))
button3= Button(cal, text= "3", padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold'),
                bg= 'powder blue' , justify= 'right', command= lambda : btnClick(3))
multiply= Button(cal, text= "X", padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold'),
                 bg= 'powder blue' , justify= 'right', command= lambda : btnClick("*"))

button0= Button(cal, text= '0', padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold'),
                bg= 'powder blue' , justify= 'right', command= lambda : btnClick(0))
clear= Button(cal, text= "c", padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold'),
                bg= 'powder blue' , justify= 'right', command=  btnClearDisplay)
equal= Button(cal, text= "=", padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold'),
                bg= 'powder blue' , justify= 'right', command= btnEqualsInput)
divide= Button(cal, text= "/", padx = 26, pady=16, bd= 8, fg= "black", font=('arial', 20 , 'bold'),
                 bg= 'powder blue' , justify= 'right', command= lambda : btnClick("/"))
entry.grid(columnspan= 4)
button7.grid(row= 1, column=0)
button8.grid(row= 1, column= 1)
button9.grid(row= 1, column= 2)
button4.grid(row= 2, column= 0)
button5.grid(row= 2, column= 1)
button6.grid(row= 2, column= 2)
button1.grid(row= 3, column= 0)
button2.grid(row= 3, column= 1)
button3.grid(row= 3, column= 2)
button0.grid(row= 4, column=0)
clear.grid(row=4, column=1)
equal.grid(row=4, column=2)
divide.grid(row=4, column=3)
add.grid(row= 1, column= 3)
subtract.grid(row=2 , column= 3)
multiply.grid(row= 3, column= 3)


cal.mainloop()
