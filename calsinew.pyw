from tkinter import *
import math


class Calc:
    def __init__(self, master):
        self.master=master
        self.master["bg"]="grey"
        self.master.title("Calculator")
        self.master.geometry()
        self.e=Entry(self.master,width=30)
        self.e.grid(row=0,column=0,columnspan=6,pady=3)
        self.e.focus_set()

        self.b1=Button(self.master,text="=",width=12,height=3,fg="White",bg="red",command=self.equals)
        self.b1.grid(row=4,column=4,columnspan=2)
        self.b2=Button(self.master, text="AC", width=5, height=3, fg="White", bg="red",command=self.clearall)
        self.b2.grid(row=1,column=4)
        self.b3=Button(self.master,text="C",width=5,height=3,fg="White",bg="red",command=self.clear1)
        self.b3.grid(row=1,column=5)
        self.b4=Button(self.master,text="+",width=5,height=3,fg="White",bg="red",command=self.add)
        self.b4.grid(row=4,column=3)
        self.b5=Button(self.master,text="*",width=5,height=3,fg="White",bg="red",command=self.multiply)
        self.b5.grid(row=2,column=3)
        self.b6=Button(self.master,text="-",width=5,height=3,fg="White",bg="red",command=self.subtract)
        self.b6.grid(row=3,column=3)
        self.b7=Button(self.master,text="/",width=5,height=3,fg="White",bg="red",command=self.divide)
        self.b7.grid(row=1,column=3)
        self.b8=Button(self.master,text="%",width=5,height=3,fg="White",bg="red",command=self.mod)
        self.b8.grid(row=4,column=2)
        self.b9=Button(self.master,text="7",width=5,height=3,fg="White",bg="red",command=self.seven)
        self.b9.grid(row=1,column=0)
        self.b10=Button(self.master,text="8",width=5,height=3,fg="White",bg="red",command=self.eight)
        self.b10.grid(row=1,column=1)
        self.b11=Button(self.master,text="9",width=5,height=3,fg="White",bg="red",command=self.nine)
        self.b11.grid(row=1,column=2)
        self.b12=Button(self.master,text="4",width=5,height=3,fg="White",bg="red",command=self.four)
        self.b12.grid(row=2,column=0)
        self.b13=Button(self.master,text="5",width=5,height=3,fg="White",bg="red",command=self.five)
        self.b13.grid(row=2,column=1)
        self.b14=Button(self.master,text="6",width=5,height=3,fg="White",bg="red",command=self.six)
        self.b14.grid(row=2,column=2)
        self.b15=Button(self.master,text="1",width=5,height=3,fg="White",bg="red",command=self.one)
        self.b15.grid(row=3,column=0)
        self.b16=Button(self.master,text="2",width=5,height=3,fg="White",bg="red",command=self.two)
        self.b16.grid(row=3,column=1)
        self.b17=Button(self.master,text="3",width=5,height=3,fg="White",bg="red",command=self.three)
        self.b17.grid(row=3,column=2)
        self.b18=Button(self.master,text="0",width=5,height=3,fg="White",bg="red",command=self.zero)
        self.b18.grid(row=4,column=0)
        self.b19=Button(self.master,text=".",width=5,height=3,fg="White",bg="red",command=self.point)
        self.b19.grid(row=4,column=1)
        self.b20=Button(self.master,text="(",width=5,height=3,fg="White",bg="red",command=self.openb)
        self.b20.grid(row=2,column=4)
        self.b21=Button(self.master,text=")",width=5,height=3,fg="White",bg="RED",command=self.closeb)
        self.b21.grid(row=2,column=5)
        self.b22=Button(self.master,text="?",width=5,height=3,fg="White",bg="red",command=self.sqrroot)
        self.b22.grid(row=3,column=4)
        self.b23=Button(self.master,text="X^2",width=5,height=3,fg="White",bg="red",command=self.square)
        self.b23.grid(row=3,column=5)
        l1=Label(self.master,text="Enter Color:",height=2,bg="grey")
        l1.grid(row=5,column=0,columnspan=2)
        self.e1 = Entry(self.master)
        self.e1.insert(END, "RED")
        self.e1.grid(row=5, column=2, columnspan=3,padx=1)
        b24=Button(self.master,text="Apply",width=4,fg="Black",bg="white",command=self.color)
        b24.grid(row=7,column=2)
        b25=Button(self.master,text="Quit",width=4,fg="Black",bg="white",command=self.finish)
        b25.grid(row=7,column=4)
        l2 = Label(self.master, text="Num colors:", height=2,bg="grey")
        l2.grid(row=6, column=0, columnspan=2)
        self.e2 = Entry(self.master)
        self.e2.insert(END, "White")
        self.e2.grid(row=6, column=2, columnspan=3,padx=1)
    def one(self):
        self.e.insert(END,"1")
    def two(self):
        self.e.insert(END, "2")
    def three(self):
        self.e.insert(END, "3")
    def four(self):
        self.e.insert(END, "4")
    def five(self):
        self.e.insert(END, "5")
    def six(self):
        self.e.insert(END, "6")
    def seven(self):
        self.e.insert(END, "7")
    def eight(self):
        self.e.insert(END, "8")
    def nine(self):
        self.e.insert(END, "9")
    def zero(self):
        self.e.insert(END, "0")
    def point(self):
        self.e.insert(END, ".")
    def openb(self):
        self.e.insert(END, "(")
    def closeb(self):
        self.e.insert(END, ")")
    def add(self):
        self.e.insert(END, "+")
    def subtract(self):
        self.e.insert(END, "-")
    def multiply(self):
        self.e.insert(END, "*")
    def divide(self):
        self.e.insert(END, "/")
    def mod(self):
        self.e.insert(END, "%")
    def getandreplace(self):
        self.newtext=self.e.get()
       # self.newtext=self.expression.replace('x','*')#expression.replace('divide','/') replace is used to change
    def equals(self):
        self.getandreplace()
        try:
            self.value=eval(self.newtext)
        except:
            self.e.delete(0,END)
            self.e.insert(0,"Invalid Syntax!!!!")
        else:
            self.e.delete(0,END)
            self.e.insert(0,self.value)
    def clearall(self):
        self.e.delete(0,END)
    def clear1(self):
        self.newtext = self.e.get() #self.text=self.e.get()[:-1]
        self.x=len(self.newtext)    #self.e.delete(0,END)
        self.e.delete(self.x-1)      #self.e.insert(0,self.text)
    def square(self):
        try:
            self.newtext=float(self.e.get())
            self.value=math.pow(self.newtext,2)
        except:
            self.e.delete(0,END)
            self.e.insert(0,"Invalid Entry!!!!")
        else:
            self.e.delete(0,END)
            self.e.insert(0,self.value)
    def sqrroot(self):
        try:
            self.newtext=float(self.e.get())
            self.value=math.sqrt(self.newtext)
        except:
            self.e.delete(0,END)
            self.e.insert(0,"Invalid Entry!!!!")
        else:
            self.e.delete(0,END)

            self.e.insert(0,self.value)
    def color(self):
        try:
            self.txt=self.e1.get()
            self.fgtxt=self.e2.get()
            self.buttons=[self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9,self.b10,self.b11,self.b12,self.b13,self.b14,self.b15,self.b16,self.b17,self.b18,self.b19,self.b20,self.b21,self.b22,self.b23]
            for i in self.buttons:
                i.configure(bg=self.txt,fg=self.fgtxt)
            self.e1.delete(0, END)
            self.e1.insert(END, self.txt)
            self.e2.delete(0, END)
            self.e2.insert(END, self.fgtxt)
        except:
            self.e1.delete(0,END)
            self.e1.insert(0,"Wrong color")
            self.e2.delete(0, END)
            self.e2.insert(0, "Wrong color")
    def finish(self):
        self.master.destroy()





root=Tk()
obj=Calc(root)
root.mainloop()
