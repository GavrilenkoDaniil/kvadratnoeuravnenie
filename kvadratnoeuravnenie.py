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
t=0
def uvel():
    global t
    if t==0:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+200))
        uvel.config(text="Уменьшить окно")
        t=1
    else:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-200))
        uvel.config(text="Увеличить окно")
        t=0

def kit():
        x1=np.arange(0, 9.5, 0.5)
        y1=(2/27)*x1**2-3
        x2=np.arange(-10, 0.5, 0.5)
        y2=(0.04)*x2**2-3
        x3=np.arange(-9, -2.5, 0.5)
        y3=(2/9)*(x3+6)**2+1
        x4=np.arange(-3, 9.5, 0.5)
        y4=(-1/12)*(x4-3)**2+6
        x5=np.arange(5, 9, 0.5)
        y5=(1/9)*(x5-5)**2+2
        x6=np.arange(5, 8.5, 0.5)
        y6=(1/8)*(x6-7)**2+1.5
        x7=np.arange(-13, -8.5, 0.5)
        y7=(-0.75)*(x7+11)**2+6
        x8=np.arange(-15, -12.5, 0.5)
        y8=(-0.5)*(x8+13)**2+3
        x9=np.arange(-15, -10, 0.5)
        y9=[1]*len(x9)
        x10=np.arange(3, 4, 0.5)
        y10=[3]*len(x10)
        fig=plt.figure()
        plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
        plt.title("Квадратное уравнение")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()

def ochki():
        x1=np.arange(-9, -1, 0.5)
        y1=-(1/16)*(x1+5)**2+2
        x2=np.arange(1, 9, 0.5)
        y2=-(1/16)*(x2-5)**2+2
        x3=np.arange(-9, -1, 0.5)
        y3=(1/4)*(x3+5)**2-3
        x4=np.arange(1, 9, 0.5)
        y4=(1/4)*(x4-5)**2-3
        x5=np.arange(-9, -6, 0.5)
        y5=-(x5+7)**2+5
        x6=np.arange(6, 9, 0.5)
        y6=-(x6-7)**2+5
        x7=np.arange(-1, 1, 0.5)
        y7=-0.5*x7**2+1.5
        fig=plt.figure()
        plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
        plt.title("Квадратное уравнение")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()

def zontik():
    x1=np.arange(-12, 12, 0.5)
    y1=-(1/18)*x1**2+12
    x2=np.arange(-4, 4, 0.5)
    y2=-(1/8)*x2**2+6
    x3=np.arange(-12, -4, 0.5)
    y3=-(1/8)*(x3+8)**2+6
    x4=np.arange(4, 12, 0.5)
    y4=-(1/8)*(x4-8)**2+6
    x5=np.arange(-4, -0.3, 0.5)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4, 0.2, 0.5)
    y6=1.5*(x6+3)**2-9
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title("Квадратное уравнение")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def babochka():
    x1=np.arange(-9, -1, 0.5)
    y1=-(1/8)*(x1+9)**2+8
    x2=np.arange(1, 9, 0.5)
    y2=-(1/8)*(x2-9)**2+8
    x3=np.arange(-9, -8, 0.5)
    y3=7*(x3+8)**2+1
    x4=np.arange(8, 9, 0.5)
    y4=7*(x4-8)**2+1
    x5=np.arange(-8, -1, 0.5)
    y5=(1/49)*(x5+1)**2
    x6=np.arange(1, 8, 0.5)
    y6=(1/49)*(x6-1)**2
    x7=np.arange(-8, -1, 0.5)
    y7=-(4/49)*(x7+1)**2
    x8=np.arange(1, 8, 0.5)
    y8=-(4/49)*(x8-1)**2
    x9=np.arange(-8, -2, 0.5)
    y9=(1/3)*(x9+5)**2-7
    x10=np.arange(2, 8, 0.5)
    y10=(1/3)*(x10-5)**2-7
    x11=np.arange(-2, -1, 0.5)
    y11=-2*(x11+1**2)-2
    x12=np.arange(1, 2, 0.5)
    y12=-2*(x12-1)**2-2
    x13=np.arange(-1, 1, 0.5)
    y13=-4*x13**2-6
    x14=np.arange(-1.5, 1.5, 0.5)
    y14=4*x14**2-6
    x15=np.arange(-1.5, 0, 0.5)
    y15=-1.5*x15+2
    x16=np.arange(0, 2, 0.5)
    y16=1.5*x16+2
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15,x16,y16)
    plt.title("Квадратное уравнение")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()
aken=Tk()
aken.title=("Квадратное уравнение")
f1=Frame(aken,width=650,height=200)
f1.pack(side=TOP)
f2=Frame(aken,width=650,height=200)
f2.pack(side=BOTTOM)
lbl=Label(f1,text="Решение квадратного уравнения",height=4,width=40,font="Arial 20",fg="green",bg="lightblue")
aken.geometry("900x450")#Минимальное разрешение окна
aken.resizable(width=False, height=False) #Запрещаю изменять разрешение окна
text1=Label(f1,text="x**2+",font="Arial 20",fg="green",justify=CENTER)
text2=Label(f1,text="x+",font="Arial 20",fg="green")
text3=Label(f1,text="=0",font="Arial 20",fg="green")
a=Entry(f1,font="Arial 20",width=5,fg="green",bg="lightblue",justify=CENTER)
b=Entry(f1,font="Arial 20",width=5,fg="green",bg="lightblue")
c=Entry(f1,font="Arial 20",width=5,fg="green",bg="lightblue")
knopka=Button(f1,text="Решить",font="Arial 20",fg="black",bg="green",height=3,width=15,relief=GROOVE,command=reshenie)
grafik=Button(f1,text="График",font="Arial 20",fg="black",bg="green",height=3,width=15,relief=GROOVE,command=graafik)
rezult=Label(f1,text="Решение",height=4,width=40,font="Arial 20",fg="black",bg="yellow")
uvel=Button(f1, text="Увеличить окно",font="Arial 20",fg="black",bg="green",height=3,width=15,relief=GROOVE,command=uvel)
var=StringVar()
var.set("Один")
r1=Radiobutton(f2, text="Кит",variable=var,value="Один",command=kit)
r2=Radiobutton(f2, text="Очки",variable=var,value="Два",command=ochki)
r3=Radiobutton(f2, text="Зонтик",variable=var,value="Три",command=zontik)
r4=Radiobutton(f2, text="Бабочка",variable=var,value="Четыре",command=babochka)
#r5=Radiobutton(f2, text="Кит",variable=var,value="Пять")

lbl.pack(side=TOP)
uvel.pack(side=BOTTOM)
rezult.pack(side=BOTTOM)
a.pack(side=LEFT)
text1.pack(side=LEFT)
b.pack(side=LEFT)
text2.pack(side=LEFT)
c.pack(side=LEFT)
text3.pack(side=LEFT)
knopka.pack(side=LEFT)
grafik.pack(side=LEFT)
r1.pack()
r2.pack()
r3.pack()
r4.pack()


aken.mainloop()