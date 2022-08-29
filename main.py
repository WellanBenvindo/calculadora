# importando tkinter
from tkinter import *
from tkinter import ttk

# cores do programa
cor1 = "#4f7df0"  # Azul
cor2 = "#626a80"  # cinza
cor3 = "#de7009"  # laranja
cor4 = "#faf9f7"  # branco

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor2)

# criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor2)
frame_corpo.grid(row=1, column=0)

# variavel todos os valores

todos_valores = " "


# criando função
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)

    # passando valor para tela
    valor_texto.set(todos_valores)

    # função para calcular


def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    print(resultado)


# função limpar tela

def limpar_tela():
    global todos_valores
    todos_valores =("")
    valor_texto.set =""

# criando label
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e",
                  justify=RIGHT, font="Ivy 18", bg="#626a80", fg="#faf9f7")
app_label.place(x=0, y=0)

# criando botões

b_1 = Button(frame_corpo,command=lambda:limpar_tela, text="C", width=11, height=2, bg="#faf9f7", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=5, height=2, bg="#faf9f7",
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=5, height=2, bg="#de7009", fg="#faf9f7",
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)
# fim botões primeira linha

# inicio botões segunda linha
b_4 = Button(frame_corpo, command=lambda: entrar_valores('7'), text="7", width=5, height=2, bg="#faf9f7",
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=55)
b_5 = Button(frame_corpo, command=lambda: entrar_valores('8'), text="8", width=5, height=2, bg="#faf9f7",
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=55)
b_6 = Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=5, height=2, bg="#faf9f7",
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=55)
b_7 = Button(frame_corpo, command=lambda: entrar_valores('*'), text="*", width=5, height=2, bg="#de7009", fg="#faf9f7",
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=55)

# inicio botões terceira linha
b_8 = Button(frame_corpo, command=lambda: entrar_valores('4'), text="4", width=5, height=2, bg="#faf9f7",
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=110)
b_9 = Button(frame_corpo, command=lambda: entrar_valores('5'), text="5", width=5, height=2, bg="#faf9f7",
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=110)
b_10 = Button(frame_corpo, command=lambda: entrar_valores('6'), text="6", width=5, height=2, bg="#faf9f7",
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=110)
b_11 = Button(frame_corpo, command=lambda: entrar_valores('-'), text="-", width=5, height=2, bg="#de7009", fg="#faf9f7",
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=110)

# inicio botões quarta linha
b_12 = Button(frame_corpo, command=lambda: entrar_valores('1'), text="1", width=5, height=2, bg="#faf9f7",
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=165)
b_13 = Button(frame_corpo, command=lambda: entrar_valores('2'), text="2", width=5, height=2, bg="#faf9f7",
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=165)
b_14 = Button(frame_corpo, command=lambda: entrar_valores('3'), text="3", width=5, height=2, bg="#faf9f7",
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=165)
b_15 = Button(frame_corpo, command=lambda: entrar_valores('+'), text="+", width=5, height=2, bg="#de7009", fg="#faf9f7",
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=165)

# Ultima Linha
b_16 = Button(frame_corpo, command=lambda: entrar_valores('0'), text="0", width=11, height=2, bg="#faf9f7",
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=220)
b_17 = Button(frame_corpo, command=lambda: entrar_valores('.'), text=".", width=5, height=2, bg="#faf9f7",
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=220)
b_18 = Button(frame_corpo, command=calcular, text="=", width=5, height=2, bg="#de7009", fg="#faf9f7",
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=220)

janela.mainloop()
