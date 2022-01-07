from tkinter import *
from math import *
def reshenie(event):
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        try:
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
        except:
            ValueError
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
    pass
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
knopka=Button(aken,text="Решить",font="Arial 20",fg="black",bg="green",height=3,width=15,relief=GROOVE)
grafik=Button(aken,text="График",font="Arial 20",fg="black",bg="green",height=3,width=15,relief=GROOVE)
knopka.bind("<Button-1>",reshenie)
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