from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

# funcionalidad de calculadora
operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_boton(numero):

    global operador # variable global porque esta por fuera de la funcion
    operador = operador + numero
    reversed_operador = operador[::-1]
    visor_calculadora.delete(0, END) # para que no se repitan  los numeros
    visor_calculadora.insert(0, reversed_operador) # para que en el visor muestre lo que se haya presionado


def borrar():

    global operador

    operador = ''

    visor_calculadora.delete(0, END)


def obtener_resultado():

    global operador

    resultado = str(eval(operador)) # almacenamos en una variable la evaluacion del operador almacenado en un string

    visor_calculadora.delete(0, END)

    visor_calculadora.insert(0, resultado) # para que en el visor muestre el resultado

    operador = ''


def revisar_checkbutton():

    x = 0

    for c in cuadros_comida:

        if variables_comida[x].get() == 1:

            cuadros_comida[x].config(state= NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()

        else:

            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')

        x += 1

    x = 0

    for c in cuadros_bebida:

        if variables_bebida[x].get() == 1:

            cuadros_bebida[x].config(state= NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()

        else:

            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')

        x += 1

    x = 0

    for c in cuadros_postres:

        if variables_postres[x].get() == 1:

            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()

        else:

            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')

        x += 1


def total():
    p = 0
    subtotal_comida = 0

    for cantidad in texto_comida:

        subtotal_comida = subtotal_comida + (float(cantidad.get()) * precios_comida[p]) # almacenamos en una variable el subtotal el cual sale de el subtotal comida + cantidad que se obtiene del entry * el precio de la lista y dejamos todo en floats

        p += 1

    p = 0
    subtotal_bebida = 0

    for cantidad in texto_comida:
        subtotal_bebida = subtotal_bebida + (float(cantidad.get()) * precios_bebida[p])

        p += 1

    p = 0
    subtotal_postres = 0

    for cantidad in texto_comida:
        subtotal_postres = subtotal_postres + (float(cantidad.get()) * precios_postres[p])

        p += 1

    subtotal = subtotal_comida + subtotal_bebida + subtotal_postres
    impuestos = subtotal * 0.07
    total_todo = subtotal + impuestos

    var_costo_comida.set(f'$ {round(subtotal_comida, 2)}')
    var_costo_bebida.set(f'$ {round(subtotal_bebida, 2)}')
    var_costo_postres.set(f'$ {round(subtotal_postres, 2)}')
    var_subtotal.set(f'$ {round(subtotal, 2)}')
    var_impuesto.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total_todo, 2)}')


def recibo():

    texto_recibo.delete(1.0, END) # para borrar
    numero_recibo = f'N# - {random.randint(1000, 9999)}' # creamos el numero del recibo
    fecha = datetime.datetime.now() # la fecha actual
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}' # ponemos la fecha en el formato deseado

    texto_recibo.insert(END, f'Datos:\t{numero_recibo}\t\t{fecha_recibo}\n') # insertamos fecha y numero de recibo
    texto_recibo.insert(END, f'*'*40 + '\n')
    texto_recibo.insert(END, f'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    x = 0
    for comida in texto_comida:

        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t${int(comida.get()) * precios_comida[x]}\n')

        x += 1

    x = 0
    for bebida in texto_bebida:

        if bebida.get() != '0':
            texto_recibo.insert(END,f'{lista_bebidas[x]}\t\t{bebida.get()}\t${int(bebida.get()) * precios_bebida[x]}\n')

        x += 1

    x = 0
    for postres in texto_postres:

        if postres.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_postres[x]}\t\t{postres.get()}\t${int(postres.get()) * precios_postres[x]}\n')

        x += 1

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de las bebidas: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de los postres: \t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Sub total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total a Pagar: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 40 + '\n')
    texto_recibo.insert(END, f'Gracias por su Visita')


def guardar_recibo():

    info_recibo = texto_recibo.get(1.0, END) # para almacenar la info del recibo en una variable
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.doc') # para guardar el archivo en una variable
    archivo.write(info_recibo)
    archivo.close()

    # informamaos al usuario
    messagebox.showinfo('Información', 'Su Recibo ha sido Guardado')


def limpiar_pantalla():

    texto_recibo.delete(1.0, END) # borramos lo que hay en el recibo

    # borramos los textos de los items
    for texto in texto_comida:

        texto.set('0')

    for texto in texto_bebida:
        texto.set('0')

    for texto in texto_postres:
        texto.set('0')

    # deshabilitamos los cuadros de texto
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)

    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)

    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    # limpiar los checkbutton
    for check in variables_comida:

        check.set(0)

    for check in variables_bebida:

        check.set(0)

    for check in variables_postres:

        check.set(0)

    # borramos las variables
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


# iniciar a tkinter
aplicacion = Tk()
aplicacion.geometry('1020x630+0+0') # tamaño de  la ventana
aplicacion.resizable(0,0) # para no maximizar
aplicacion.title('Mi Restaurante - Sistema de Facturación') # para el titulo
aplicacion.iconbitmap('img\\restaurante.ico') # para el icono
aplicacion.config(bg = 'CadetBlue') # para el fondo
#aplicacion.overrideredirect(True) # ventana sin botones ni titulos e iconos

# frame superior
frame_superior = Frame(aplicacion, bd= 2, relief=FLAT) # declaramos el Frame
frame_superior.pack(side= TOP) # mostramos el Frame

# etiqueta titulo
etiqueta_titulo = Label(frame_superior) # creamos la etiqueta
etiqueta_titulo.config(font=('Verdana', 40, 'bold'),
                       fg='white',
                       bg='CadetBlue',
                       width=27,
                       text='Sistema de Facturación') # personalizamos la eftiqueta
etiqueta_titulo.grid(row=0, column=0) # posicionamos la etiqueta

# frame izq
frame_izquierdo = Frame(aplicacion, bd= 2, relief=FLAT) # declaramos el Frame
frame_izquierdo.pack(side= LEFT)  # mostramos el Frame

# panel costos
frame_costos = Frame(frame_izquierdo, bd= 2, relief=FLAT, padx= 10, bg='CadetBlue') # declaramos el Frame
frame_costos.pack(side= BOTTOM)  # mostramos el Frame

# frame comidas
frame_comidas = LabelFrame(frame_izquierdo, # declaramos el labelFrame
                           text= 'Comidas',
                           font=('Verdana', 16, 'bold'),
                           fg= 'CadetBlue',
                           bd= 2,
                           relief= FLAT,) # damos formato
frame_comidas.pack(side= LEFT) # lo mostramos

# frame Bebidas
frame_Bebidas = LabelFrame(frame_izquierdo,
                           text= 'Bebidas',
                           font=('Verdana', 16, 'bold'),
                           fg= 'CadetBlue',
                           bd= 2,
                           relief= FLAT,)
frame_Bebidas.pack(side= LEFT)

# frame Postres
frame_Postres = LabelFrame(frame_izquierdo,
                           text= 'Postres',
                           font=('Verdana', 16, 'bold'),
                           fg= 'CadetBlue',
                           bd= 2,
                           relief= FLAT,)
frame_Postres.pack(side= LEFT)

# frame derecha
frame_derecha = Frame(aplicacion, bd=2, relief=FLAT) # declaramos el Frame
frame_derecha.pack(side= RIGHT) # mostramos el Frame

# frame calculadora
frame_calculadora = Frame(frame_derecha, bd=2, relief=FLAT, bg='CadetBlue') # declaramos el Frame
frame_calculadora.pack(side= TOP) # mostramos el Frame

# frame recibo
frame_recibo = Frame(frame_derecha, bd=2, relief=FLAT, bg='CadetBlue') # declaramos el Frame
frame_recibo.pack(side= TOP) # mostramos el Frame

# frame botones
frame_botones = Frame(frame_derecha, bd=2, relief=FLAT, bg='CadetBlue', padx = 42) # declaramos el Frame
frame_botones.pack(side= TOP) # mostramos el Frame

# lista de productos
lista_comidas = ['Pollo', 'Cordero', 'Salmon', 'Merluza', 'Kebab', 'Pizza1', 'Pizza2', 'Pizza3']
lista_bebidas = ['Agua', 'Soda', 'Jugo', 'Cola', 'Vino1', 'Vino2', 'Cerveza1', 'Cerveza2']
lista_postres = ['Helado', 'Frutas', 'Brownies', 'Flan', 'Mousse', 'Pastel1', 'Pastel2', 'Pastel3']

# loop para crear un checkbutton y los items comidas
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:

    # crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(frame_comidas,
                         text= comida.title(),
                         font=('Verdana', 12, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable= variables_comida[contador],
                         command= revisar_checkbutton) # llamamos a la fincion para que el check funcione
    comida.grid(row=contador,
                column= 0,
                sticky= W)

    # crear los cuadros de entrada
    cuadros_comida.append('') # asi vacio con fines de que exista
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(frame_comidas,
                                     font=('Verdana', 12, 'bold'),
                                     width=6,
                                     state=DISABLED,
                                     bd= 2,
                                     textvariable= texto_comida[contador])

    cuadros_comida[contador].grid(row= contador,
                                  column = 1,
                                  sticky= W)

    contador += 1

# loop para crear un checkbutton y los items comidas
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:

    # crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(frame_Bebidas,
                         text= bebida.title(),
                         font=('Verdana', 12, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         bd= 2,
                         variable= variables_bebida[contador],
                         command=revisar_checkbutton)  # llamamos a la fincion para que el check funcione
    bebida.grid(row=contador,
                column= 0,
                sticky= W)

    # crear los cuadros de entrada
    cuadros_bebida.append('')  # asi vacio con fines de que exista
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(frame_Bebidas,
                                     font=('Verdana', 12, 'bold'),
                                     width=6,
                                     state=DISABLED,
                                     bd=2,
                                     textvariable=texto_bebida[contador])

    cuadros_bebida[contador].grid(row=contador,
                                  column=1,
                                  sticky=W)

    contador += 1

# loop para crear un checkbutton y los items comidas
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:

    # crear checkbutton
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(frame_Postres,
                         text= postres.title(),
                         font=('Verdana', 12, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable= variables_postres[contador],
                         command=revisar_checkbutton)  # llamamos a la fincion para que el check funcione
    postres.grid(row=contador,
                 column= 0,
                 sticky= W)

    # crear los cuadros de entrada
    cuadros_postres.append('')  # asi vacio con fines de que exista
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(frame_Postres,
                                     font=('Verdana', 12, 'bold'),
                                     width=6,
                                     state=DISABLED,
                                      bd= 2,
                                     textvariable=texto_postres[contador])

    cuadros_postres[contador].grid(row=contador,
                                  column=1,
                                  sticky=W)

    contador += 1

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(frame_costos,
                              font=('Verdana', 10, 'bold'),
                              fg='white',
                              text= 'Costo Comida',
                              bg= 'CadetBlue')
etiqueta_costo_comida.grid(row= 0, column=0)
texto_costo_comida = Entry(frame_costos,
                           font=('Verdana', 12, 'bold'),
                           fg= 'CadetBlue',
                           width= 8,
                           state= 'readonly',
                           textvariable= var_costo_comida)
texto_costo_comida.grid(row= 0, column= 1, padx= 41, pady = 2)

# etiquetas de costo y campos de entrada
etiqueta_costo_bebida = Label(frame_costos,
                              font=('Verdana', 10, 'bold'),
                              fg='white',
                              text= 'Costo Bebidas',
                              bg= 'CadetBlue')
etiqueta_costo_bebida.grid(row= 1, column=0)
texto_costo_bebida = Entry(frame_costos,
                           font=('Verdana', 12, 'bold'),
                           fg= 'CadetBlue',
                           width= 8,
                           state= 'readonly',
                           textvariable= var_costo_bebida)
texto_costo_bebida.grid(row= 1, column= 1, padx= 41, pady = 2)

# etiquetas de costo y campos de entrada
etiqueta_costo_postres = Label(frame_costos,
                              font=('Verdana', 10, 'bold'),
                              fg='white',
                              text= 'Costo Postres',
                              bg= 'CadetBlue')
etiqueta_costo_postres.grid(row= 2, column= 0)
texto_costo_postres = Entry(frame_costos,
                           font=('Verdana', 12, 'bold'),
                           fg= 'CadetBlue',
                           width= 8,
                           state= 'readonly',
                           textvariable= var_costo_postres)
texto_costo_postres.grid(row= 2, column= 1, padx= 41, pady = 2)

# etiquetas de costo y campos de entrada
etiqueta_subtotal = Label(frame_costos,
                              font=('Verdana', 10, 'bold'),
                              fg='white',
                              text= 'SubTotal',
                              bg= 'CadetBlue')
etiqueta_subtotal.grid(row= 0, column= 2)
texto_subtotal = Entry(frame_costos,
                           font=('Verdana', 12, 'bold'),
                           fg= 'CadetBlue',
                           width= 8,
                           state= 'readonly',
                           textvariable= var_subtotal)
texto_subtotal.grid(row= 0, column= 3, padx= 41, pady = 2)

# etiquetas de costo y campos de entrada
etiqueta_impuesto = Label(frame_costos,
                              font=('Verdana', 10, 'bold'),
                              fg='white',
                              text= 'Impuesto',
                              bg= 'CadetBlue')
etiqueta_impuesto.grid(row= 1, column= 2)
texto_impuesto = Entry(frame_costos,
                           font=('Verdana', 12, 'bold'),
                           fg= 'CadetBlue',
                           width= 8,
                           state= 'readonly',
                           textvariable= var_impuesto)
texto_impuesto.grid(row= 1, column= 3, padx= 41, pady = 2)

# etiquetas de costo y campos de entrada
etiqueta_var_total = Label(frame_costos,
                              font=('Verdana', 10, 'bold'),
                              fg='white',
                              text = 'Total',
                              bg= 'CadetBlue')
etiqueta_var_total.grid(row= 2, column= 2)
etiqueta_var_total = Entry(frame_costos,
                           font=('Verdana', 12, 'bold'),
                           fg= 'CadetBlue',
                           width= 8,
                           state= 'readonly',
                           textvariable= var_total)
etiqueta_var_total.grid(row= 2, column= 3, padx= 32, pady = 2)

# creamos los botones
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []

columnas = 0

for boton in botones:

    boton = Button(frame_botones,
                   font=('Verdana', 10, 'bold'),
                   bg= 'CadetBlue',
                   activebackground='CadetBlue3',
                   width= 8,
                   fg= 'White',
                   activeforeground= 'Yellow',
                   text= boton)

    botones_creados.append(boton)

    boton.grid(row = 0,
               column= columnas,
               padx = 4,
               pady = 3)

    columnas += 1

botones_creados[0].config(command= total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar_recibo)
botones_creados[3].config(command=limpiar_pantalla)

# area de recibo
texto_recibo = Text(frame_recibo,
                    font= ('Verdana', 12, 'bold'),
                    bd= 2,
                    width=40,
                    height= 10)

texto_recibo.grid(row = 0,
                  column = 0)

# calculadora
visor_calculadora = Entry(frame_calculadora,
                          font=('verdana', 16, 'bold'),
                          width= 29,
                          bd= 2)
visor_calculadora.grid(row= 0, column = 0, columnspan= 4)

# botones de calculadora
botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','X','CE','Borrar', '0', '/']
botones_guardados = []

fila = 1
columnas = 0

for boton_cal in botones_calculadora:

    boton_cal = Button(frame_calculadora,
                   font=('Verdana', 12, 'bold'),
                   bg= 'CadetBlue',
                   activebackground='CadetBlue3',
                   fg='White',
                   activeforeground='Yellow',
                   text= boton_cal,
                   width= 9,
                   bd= 2)

    botones_guardados.append(boton_cal)

    boton_cal.grid(row = fila,
               column = columnas)

    if columnas == 3:

        fila += 1

    columnas += 1

    if columnas == 4:

        columnas = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command= obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))

# evitar el cierre de la pantalla
aplicacion.mainloop()