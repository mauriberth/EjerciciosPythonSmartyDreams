print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");
#Importaciones de librerías para el proyecto
from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

#BASE DEL CONOCIMIENTO (TAMBIÉN PUEDE OBTENERSE DEL ARCHIVO .TXT LISTA_PRECIOS)
op = ''
PComida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
PBeb = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
PPost = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

#DEFINICION DE FUNCIONES
def ClickB(num):
    global op
    op = op + num
    VCalculadora.delete(0, END)
    VCalculadora.insert(END, op)

def borrar():
    global op
    op = ''
    VCalculadora.delete(0, END)

def ObtRes():
    global op
    resultado = str(eval(op))
    VCalculadora.delete(0, END)
    VCalculadora.insert(0, resultado)
    op = ''

def VerifCheck():
    x = 0
    for c in CuadrosC:
        if varCom[x].get() == 1:
            CuadrosC[x].config(state=NORMAL)
            if CuadrosC[x].get() == '0':
                CuadrosC[x].delete(0, END)
            CuadrosC[x].focus()
        else:
            CuadrosC[x].config(state=DISABLED)
            txtCom[x].set('0')
        x += 1

    x = 0
    for c in CuadrosB:
        if varBeb[x].get() == 1:
            CuadrosB[x].config(state=NORMAL)
            if CuadrosB[x].get() == '0':
                CuadrosB[x].delete(0, END)
            CuadrosB[x].focus()
        else:
            CuadrosB[x].config(state=DISABLED)
            txtBeb[x].set('0')
        x += 1

    x = 0
    for c in CuadrosP:
        if varPost[x].get() == 1:
            CuadrosP[x].config(state=NORMAL)
            if CuadrosP[x].get() == '0':
                CuadrosP[x].delete(0, END)
            CuadrosP[x].focus()
        else:
            CuadrosP[x].config(state=DISABLED)
            txtPost[x].set('0')
        x += 1

def total():
    SubTCom = 0
    p = 0
    for cant in txtCom:
        SubTCom = SubTCom + (float(cant.get()) * PComida[p])
        p += 1

    SubTBeb = 0
    p = 0
    for cant in txtBeb:
        SubTBeb = SubTBeb + (float(cant.get()) * PBeb[p])
        p += 1

    SubTPost = 0
    p = 0
    for cant in txtPost:
        SubTPost = SubTPost + (float(cant.get()) * PPost[p])
        p += 1

    subTotal = SubTCom + SubTBeb + SubTPost
    imp = subTotal * 0.07
    total = subTotal + imp

    VCCom.set(f'$ {round(SubTCom, 2)}')
    VCBeb.set(f'$ {round(SubTBeb, 2)}')
    VCBeb.set(f'$ {round(SubTPost, 2)}')
    VSubT.set(f'$ {round(subTotal, 2)}')
    VImp.set(f'$ {round(imp, 2)}')
    VTotal.set(f'$ {round(total, 2)}')

def recibo():
    txtRecibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    txtRecibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    txtRecibo.insert(END, f'*' * 47 + '\n')
    txtRecibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    txtRecibo.insert(END, f'-' * 54 + '\n')

    x = 0
    for comida in txtCom:
        if comida.get() != '0':
            txtRecibo.insert(END, f'{ComidasList[x]}\t\t{comida.get()}\t'
                                     f'$ {int(comida.get()) * PComida[x]}\n')
        x += 1

    x = 0
    for bebida in txtBeb:
        if bebida.get() != '0':
            txtRecibo.insert(END, f'{BebidasList[x]}\t\t{bebida.get()}\t'
                                     f'$ {int(bebida.get()) * PBeb[x]}\n')
        x += 1

    x = 0
    for postres in txtPost:
        if postres.get() != '0':
            txtRecibo.insert(END, f'{PostresList[x]}\t\t{postres.get()}\t'
                                     f'$ {int(postres.get()) * PPost[x]}\n')
        x += 1

    txtRecibo.insert(END, f'-' * 54 + '\n')
    txtRecibo.insert(END, f' Costo de la Comida: \t\t\t{VCCom.get()}\n')
    txtRecibo.insert(END, f' Costo de la Bebida: \t\t\t{VCBeb.get()}\n')
    txtRecibo.insert(END, f' Costo de la Postres: \t\t\t{VCBeb.get()}\n')
    txtRecibo.insert(END, f'-' * 54 + '\n')
    txtRecibo.insert(END, f' Sub-total: \t\t\t{VSubT.get()}\n')
    txtRecibo.insert(END, f' imp: \t\t\t{VImp.get()}\n')
    txtRecibo.insert(END, f' Total: \t\t\t{VTotal.get()}\n')
    txtRecibo.insert(END, f'*' * 47 + '\n')
    txtRecibo.insert(END, 'Lo esperamos pronto')

def guardar():
    info_recibo = txtRecibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')

def resetear():
    txtRecibo.delete(0.1, END)

    for texto in txtCom:
        texto.set('0')
    for texto in txtBeb:
        texto.set('0')
    for texto in txtPost:
        texto.set('0')

    for cuadro in CuadrosC:
        cuadro.config(state=DISABLED)
    for cuadro in CuadrosB:
        cuadro.config(state=DISABLED)
    for cuadro in CuadrosP:
        cuadro.config(state=DISABLED)

    for v in varCom:
        v.set(0)
    for v in varBeb:
        v.set(0)
    for v in varPost:
        v.set(0)

    VCCom.set('')
    VCBeb.set('')
    VCBeb.set('')
    VSubT.set('')
    VImp.set('')
    VTotal.set('')

# VENTANA
aplicacion = Tk()
aplicacion.geometry('1020x630+0+0')
aplicacion.resizable(0, 0)
aplicacion.title("MauriBurguers - Facturación")
aplicacion.config(bg='burlywood')

# ARRIBA P
SupP = Frame(aplicacion, bd=1, relief=FLAT)
SupP.pack(side=TOP)

# TITULO ET
ETitulo = Label(SupP, text='Mauriburguers', fg='azure3',
                        font=('Dosis', 58), bg='burlywood', width=27)
ETitulo.grid(row=0, column=0)

# LEFT P
IzqP = Frame(aplicacion, bd=1, relief=FLAT)
IzqP.pack(side=LEFT)

# COSTOS P
CostosP = Frame(IzqP, bd=1, relief=FLAT, bg='azure4', padx=50)
CostosP.pack(side=BOTTOM)

# COMIDAS P
ComidasP = LabelFrame(IzqP, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
ComidasP.pack(side=LEFT)

# BEBIDAS P
panel_bebidas = LabelFrame(IzqP, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# POSTRES P
PostresP = LabelFrame(IzqP, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
PostresP.pack(side=LEFT)

# RIGHT P
DerP = Frame(aplicacion, bd=1, relief=FLAT)
DerP.pack(side=RIGHT)

# CALCULADORA P
CalcuP = Frame(DerP, bd=1, relief=FLAT, bg='burlywood')
CalcuP.pack()

# TICKET P
ticketP = Frame(DerP, bd=1, relief=FLAT, bg='burlywood')
ticketP.pack()

# BOTONES P
BttnsP = Frame(DerP, bd=1, relief=FLAT, bg='burlywood')
BttnsP.pack()

# PRODUCTOS DISPONIBLES
ComidasList = ['pollo', 'coredero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
BebidasList = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
PostresList = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# ITEMS COMIDA
varCom = []
CuadrosC = []
txtCom = []
contador = 0
for comida in ComidasList:
    # CHECKBTTN
    varCom.append('')
    varCom[contador] = IntVar()
    comida = Checkbutton(ComidasP,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold',),
                         onvalue=1,
                         offvalue=0,
                         variable=varCom[contador],
                         command=VerifCheck)

    comida.grid(row=contador,
                column=0,
                sticky=W)

    # CUADROS ENTRADA
    CuadrosC.append('')
    txtCom.append('')
    txtCom[contador] = StringVar()
    txtCom[contador].set('0')
    CuadrosC[contador] = Entry(ComidasP,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=txtCom[contador])
    CuadrosC[contador].grid(row=contador,
                                  column=1)
    contador += 1

# ITEMS BEBIDA
varBeb = []
CuadrosB = []
txtBeb = []
contador = 0
for bebida in BebidasList:
    # CHECKBTTN
    varBeb.append('')
    varBeb[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold',),
                         onvalue=1,
                         offvalue=0,
                         variable=varBeb[contador],
                         command=VerifCheck)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # CUADROS ENTRADA
    CuadrosB.append('')
    txtBeb.append('')
    txtBeb[contador] = StringVar()
    txtBeb[contador].set('0')
    CuadrosB[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=txtBeb[contador])
    CuadrosB[contador].grid(row=contador,
                                  column=1)

    contador += 1

# ITEMS POSTRES
varPost = []
CuadrosP = []
txtPost = []
contador = 0
for postres in PostresList:
    # CHECKBTTN
    varPost.append('')
    varPost[contador] = IntVar()
    postres = Checkbutton(PostresP,
                          text=postres.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=varPost[contador],
                         command=VerifCheck)
    postres.grid(row=contador,
                 column=0,
                 sticky=W)

    # CUADROS ENTRADA
    CuadrosP.append('')
    txtPost.append('')
    txtPost[contador] = StringVar()
    txtPost[contador].set('0')
    CuadrosP[contador] = Entry(PostresP,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=txtPost[contador])
    CuadrosP[contador].grid(row=contador,
                                   column=1)
    contador += 1


# VARS
VCCom = StringVar()
VCBeb = StringVar()
VCBeb = StringVar()
VSubT = StringVar()
VImp = StringVar()
VTotal = StringVar()

# etiquetas de costo y campos de entrada
ECCom = Label(CostosP,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
ECCom.grid(row=0, column=0)

txtCComida = Entry(CostosP,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=VCCom)
txtCComida.grid(row=0, column=1, padx=41)

ECBeb = Label(CostosP,
                              text='Costo Bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
ECBeb.grid(row=1, column=0)

txtCBebida = Entry(CostosP,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=VCBeb)
txtCBebida.grid(row=1, column=1, padx=41)

ECPost = Label(CostosP,
                              text='Costo Postres',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
ECPost.grid(row=2, column=0)

txtCPost = Entry(CostosP,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=VCBeb)
txtCPost.grid(row=2, column=1, padx=41)

ESubT = Label(CostosP,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
ESubT.grid(row=0, column=2)

txtSubT = Entry(CostosP,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=VSubT)
txtSubT.grid(row=0, column=3, padx=41)

EImp = Label(CostosP,
                              text='imp',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
EImp.grid(row=1, column=2)

txtImp = Entry(CostosP,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=VImp)
txtImp.grid(row=1, column=3, padx=41)

ETotal = Label(CostosP,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
ETotal.grid(row=2, column=2)

txtTotal = Entry(CostosP,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=VTotal)
txtTotal.grid(row=2, column=3, padx=41)

#BTTNS
botones = ['total', 'recibo', 'guardar', 'resetear']
BttnsC = []

columnas = 0
for boton in botones:
    boton = Button(BttnsP,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)

    BttnsC.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas += 1

BttnsC[0].config(command=total)
BttnsC[1].config(command=recibo)
BttnsC[2].config(command=guardar)
BttnsC[3].config(command=resetear)

#TICKET O RECIBO
txtRecibo = Text(ticketP,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
txtRecibo.grid(row=0,
                  column=0)

#CALCULADORA
VCalculadora = Entry(CalcuP,
                          font=('Dosis', 16, 'bold'),
                          width=32,
                          bd=1)
VCalculadora.grid(row=0,
                       column=0,
                       columnspan=4)

BttnsCalcu = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', 'x', 'R', 'B', '0', '/']
botones_guardados = []

fila = 1
columna = 0
for boton in BttnsCalcu:
    boton = Button(CalcuP,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)

    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : ClickB('7'))
botones_guardados[1].config(command=lambda : ClickB('8'))
botones_guardados[2].config(command=lambda : ClickB('9'))
botones_guardados[3].config(command=lambda : ClickB('+'))
botones_guardados[4].config(command=lambda : ClickB('4'))
botones_guardados[5].config(command=lambda : ClickB('5'))
botones_guardados[6].config(command=lambda : ClickB('6'))
botones_guardados[7].config(command=lambda : ClickB('-'))
botones_guardados[8].config(command=lambda : ClickB('1'))
botones_guardados[9].config(command=lambda : ClickB('2'))
botones_guardados[10].config(command=lambda : ClickB('3'))
botones_guardados[11].config(command=lambda : ClickB('*'))
botones_guardados[12].config(command=ObtRes)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : ClickB('0'))
botones_guardados[15].config(command=lambda : ClickB('/'))

#Para que no se cierre la pantalla.
aplicacion.mainloop()
