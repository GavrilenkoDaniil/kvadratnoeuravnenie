from tkinter import *

def reshenie(event):
    pass
aken=Tk()
aken.title=("Квадратное уравнение")
lbl=Label(aken,text="Решение квадратного уравнения",height=4,width=40,font="Arial 20",fg="green",bg="lightblue")
aken.geometry("900x600")
text1=Label(aken,text="x**2+",font="Arial 20",fg="green",justify=CENTER)
text2=Label(aken,text="x+",font="Arial 20",fg="green")
text3=Label(aken,text="=0",font="Arial 20",fg="green")
a=Entry(aken,font="Arial 20",width=5,fg="green",bg="lightblue",justify=CENTER)
b=Entry(aken,font="Arial 20",width=5,fg="green",bg="lightblue")
c=Entry(aken,font="Arial 20",width=5,fg="green",bg="lightblue")
knopka=Button(aken,text="Решить",font="Arial 20",fg="black",bg="green",height=3,width=15,relief=GROOVE)
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
aken.mainloop()