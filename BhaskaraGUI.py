import math
from tkinter import *

janela = Tk()

def calc():
    num_a1 = int(num_a.get())
    num_b1 = int(num_b.get())
    num_c1 = int(num_c.get())
    delt = num_b1**2 - 4*num_a1*num_c1
    delta_l["text"]="Delta = ", delt
    x1 = - num_b1 + math.sqrt(delt)
    x2 = - num_b1 - math.sqrt(delt)

    x1_r["text"]="x1 = ", x1
    x2_r["text"]="x2 = ", x2


model = Label(janela, text="Siga o modelo: ax²+bx+c=0")
model.place(x=75, y=15)

num_a = Entry(janela, width="5")
num_a.place(x=40, y=100)

num_b = Entry(janela, width="5")
num_b.place(x=40, y=150)

num_c = Entry(janela, width="5")
num_c.place(x=40, y=200)

ax = Label(janela, text="a =")
ax.place(x=20, y=100)

bx = Label(janela, text="b =")
bx.place(x=20, y=150)

cx = Label(janela, text="c =")
cx.place(x=20, y=200)

delta_l = Label(janela)
delta_l.place(x=170, y=100)

x1_r = Label(janela)
x1_r.place(x=170, y=150)

x2_r = Label(janela)
x2_r.place(x=170, y=180)

result = Label(janela)
result.place(x=170, y=200)

start = Button(janela, width="20", text="Calcular", command=calc)
start.place(x=80 ,y=300)


janela.geometry("300x400+760+220")
janela.title("Equação do segundo grau - Bháskara")
janela.mainloop()