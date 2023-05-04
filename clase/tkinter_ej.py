from tkinter import *

# ------------------------------
#          Interfaz Grafica
# ------------------------------
raiz = Tk() # Crea la ventana principal
raiz.title('GIU - Com 22616') # titulo de la ventana
raiz.resizable(height=0, width=0)


# ------- Barra Menu ----------
barramenu = Menu(raiz) # Creo la barra menu
raiz.config(menu=barramenu) # Agrego el menu a la pantalla

bbddmenu = Menu(barramenu, tearoff=0)
bbddmenu.add_command(label="Conectar")
bbddmenu.add_command(label="Salir")
barramenu.add_cascade(label="BBDD", menu=bbddmenu)

limpiarmenu = Menu(barramenu, tearoff=0)
limpiarmenu.add_command(label="Limpiar campos")
barramenu.add_cascade(label='Limpiar', menu=limpiarmenu)

ayudamenu = Menu(barramenu, tearoff=0)
ayudamenu.add_command(label='Licencia')
ayudamenu.add_command(label='Acerca de..')
barramenu.add_cascade(label='Ayuda', menu=ayudamenu)

# ---------- Frame Campos -------------------
framecampos = Frame(raiz) # Creo el frame campos
framecampos.pack()

legajo = StringVar()
alumno  = StringVar()
email = StringVar()
calificacion = DoubleVar()
escuela = StringVar()
localidad = StringVar()
provincia = StringVar()

'''
entero = IntVar()  # Declara variable de tipo entera
flotante = DoubleVar()  # Declara variable de tipo flotante
cadena = StringVar()  # Declara variable de tipo cadena
booleano = BooleanVar()  # Declara variable de tipo booleana
'''

legajo_input = Entry(framecampos, textvariable=legajo)
legajo_input.grid(row=0, column=2, padx=10, pady=10)

alumno_input = Entry(framecampos, textvariable=alumno) 
alumno_input.grid(row=1, column=2, padx=10, pady=10)

email_input = Entry(framecampos, textvariable=email)
email_input.grid(row=2, column=2, padx=10, pady=10)

calificacion_input = Entry(framecampos, textvariable=calificacion)
calificacion_input.grid(row=3, column=2, padx=10, pady=10)

escuela_input = Entry(framecampos, textvariable=escuela)
escuela_input.grid(row=4, column=2, padx=10, pady=10)

localidad_input = Entry(framecampos, textvariable=localidad)
localidad_input.grid(row=5, column=2, padx=10, pady=10)

provincia_input = Entry(framecampos, textvariable=provincia)
provincia_input.grid(row=6, column=2, padx=10, pady=10)

# labels
'''
"STICKY"
     n
  nw   ne
w         e
  sw   se
     s
'''

legajo_label = Label(framecampos, text='Legajo:')
legajo_label.grid(row=0, column=1, padx=10, pady=10, sticky='e')

alumno_label = Label(framecampos, text='Alumno:')
alumno_label.grid(row=1, column=1, padx=10, pady=10, sticky='e')

email_label = Label(framecampos, text='Email:')
email_label.grid(row=2, column=1, padx=10, pady=10, sticky='e')

calificacion_label = Label(framecampos, text='Calificación:')
calificacion_label.grid(row=3, column=1, padx=10, pady=10, sticky='e')

escuela_label = Label(framecampos, text='Escuela:')
escuela_label.grid(row=4, column=1, padx=10, pady=10, sticky='e')

localidad_label = Label(framecampos, text='Localidad:')
localidad_label.grid(row=5, column=1, padx=10, pady=10, sticky='e')

provincia_label = Label(framecampos, text='Provincia:')
provincia_label.grid(row=6, column=1, padx=10, pady=10, sticky='e')

# ----------- FRAME BOTONES -*---------------
# CRUD = Create, read, update, delete
framebotones = Frame(raiz)
framebotones.pack()

boton_crear = Button(framebotones, text='Crear')
boton_crear.grid(row=0, column=0, padx=5, pady=10)

boton_leer = Button(framebotones, text='leer')
boton_leer.grid(row=0, column=1, padx=5, pady=10)

boton_actualizar = Button(framebotones, text='actualizar')
boton_actualizar.grid(row=0, column=2, padx=5, pady=10)

boton_borrar = Button(framebotones, text='borrar')
boton_borrar.grid(row=0, column=3, padx=5, pady=10)

# ------------ Frame Copy ------------------
framecopy = Frame(raiz)
framecopy.pack()

copy_label = Label(framecopy, text='(2022) Creado por Matias Escobar para CaC 4.0 - BigData')
copy_label.grid(row=0, column=0, padx=10, pady=10)

# ----- ULTIMA LINEA DEL PROGRAMA -----------
raiz.mainloop() # Mantiene abierta la ventana
