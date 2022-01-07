from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
global D,t,graf
D=-1
t="нет решений!"
graf=False
def reshenie():
    global D,t,graf
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        if float(a.get())==0 and float(b.get())==0 and float(c.get())==0:
            rezult.configure(text=f"Тут не может быть 0")
            a.configure(bg="red")
            b.configure(bg="red")
            c.configure(bg="red")
            graf=False
        elif float(a.get())==0 and float(b.get())!=0 and float(c.get())!=0:
            b_=float(b.get())
            c_=float(c.get())
            x1_=round((-1*c_)/b_,2)
            t=f"X1={x1_}"
            rezult.configure(text=f"{t}")
            graf=False
        elif float(a.get())!=0:
            a_=float(a.get())
            b_=float(b.get())
            c_=float(c.get())
            D=b_*b_-4*a_*c_
            if D>0:
                x1_=round((-1*b_+sqrt(D))/(2*a_),2)
                x2_=round((-1*b_-sqrt(D))/(2*a_),2)
                t=f"X1={x1_}, \nX2={x2_}"
                graf=True
            elif D==0:
                x1_=round((-1*b_)/(2*a_),2)
                t=f"X1={x1_}"
                graf=True
            else:
                t="Корней нет"
                graf=False
            rezult.configure(text=f"D={D}\n{t}")
            a.configure(bg="lightblue")
            b.configure(bg="lightblue")
            c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
    return graf,D,t

def graafik():
    graf,D,t=reshenie()
    if graf==True:
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x=np.arange(x0-10, x0+10, 0.5)#min max step
        y=a_*x*x+b_*x+c_
        fig=plt.figure()
        plt.plot(x,y,"b:o",x0,y0,"r-d")
        plt.title("Квадратное уравнение")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График невозможно построить"
    rezult.configure(text=f"D={D}\n{t}\n{text}")
aken=Tk()
aken.title=("Квадратное уравнение")
lbl=Label(aken,text="Решение квадратного уравнения",height=4,width=40,font="Arial 20",fg="green",bg="lightblue")
aken.minsize(900,400)#Минимальное разрешение окна
aken.resizable(width=False, height=False) #Запрещаю изменять разрешение окна
text1=Label(aken,text="x**2+",font="Arial 20",fg="green",justify=CENTER)
text2=Label(aken,text="x+",font="Arial 20",fg="green")
text3=Label(aken,text="=0",font="Arial 20",fg="green")
a=Entry(aken,font="Arial 20",width=5,fg="green",bg="lightblue",justify=CENTER)
b=Entry(aken,font="Arial 20",width=5,fg="green",bg="lightblue")
c=Entry(aken,font="Arial 20",width=5,fg="green",bg="lightblue")
knopka=Button(aken,text="Решить",font="Arial 20",fg="black",bg="green",height=3,width=15,relief=GROOVE,command=reshenie)
grafik=Button(aken,text="График",font="Arial 20",fg="black",bg="green",height=3,width=15,relief=GROOVE,command=graafik)
rezult=Label(aken,text="Решение",height=4,width=40,font="Arial 20",fg="black",bg="yellow")
lbl.pack(side=TOP)
rezult.pack(side=BOTTOM)
a.pack(side=LEFT)
text1.pack(side=LEFT)
b.pack(side=LEFT)
text2.pack(side=LEFT)
c.pack(side=LEFT)
text3.pack(side=LEFT)
knopka.pack(side=LEFT)
grafik.pack(side=LEFT)

aken.mainloop()