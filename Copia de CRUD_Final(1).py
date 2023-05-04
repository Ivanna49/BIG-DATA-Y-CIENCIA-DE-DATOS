from tkinter import *
import sqlite3 as sq3
from tkinter import messagebox

# ------------------------------
#       Funcionalidades 
# ------------------------------

#Menu
#MenuBBDD
def conectar():
  global con
  global cur
  con = sq3.connect('mi_db.db')
  cur = con.cursor()
  messagebox.showinfo('STATUS', 'Conectado a la BBDD')

def salir():
  resp = messagebox.askquestion('Confirmar', '¿Desea Salir del programa?')
  if resp == "yes":
    con.close()     # Desconecta la BBDD
    raiz.destroy()  # Cierra el Programa

def licencia():
  # CREATIVE COMMONS GNU GPL https://www.gnu.org/licenses/gpl-3.0.txt  
  gnu = '''
    Demo de un sistema CRUD en Python para gestión 
    de alumnos
    Copyright (C) 2022 - Matias Escobar
    Email: matias.escobar@bue.edu.ar
    \n ===============================
    This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
    '''
  
  messagebox.showinfo('Licencia', gnu)

def acerca():
    messagebox.showinfo("Acerca de..", "Creado por Matias Escobar \npara Codo a Codo 4.0 - Big Data")
    
# ------------- CRUD -----------
def buscar_escuela(actualiza):
    con = sq3.connect('mi_db.db')
    cur = con.cursor()
    if actualiza == True:
        cur.execute('SELECT _id, localidad, provincia FROM escuelas WHERE nombre = ?', (escuela.get(),))
    else:
        cur.execute('SELECT nombre FROM escuelas')
    
    resultado = cur.fetchall()
    # print(resultado)
    retorno = []
    for e in resultado:
        if actualiza == True:
            provincia.set(e[2])
            localidad.set(e[1])
        retorno.append(e[0])
    
    con.close()
    return retorno

def leer():
    query_leer = '''SELECT alumnos.legajo, alumnos.nombre, alumnos.nota, alumnos.email, alumnos.grado, escuelas.nombre, escuelas.localidad, escuelas.provincia 
    FROM alumnos INNER JOIN escuelas
    ON alumnos.id_escuela = escuelas._id WHERE alumnos.legajo ='''
    cur.execute(query_leer + legajo.get())
    resultado = cur.fetchall()
    #print(resultado)
    if resultado == []:
        messagebox.showerror('ERROR', 'No existe ese número de legajo')
    else:
        for e in resultado:
            legajo.set(e[0])
            alumno.set(e[1])
            calificacion.set(e[2])
            email.set(e[3])
            escuela.set(e[5])
            localidad.set(e[6])
            provincia.set(e[7])
            legajo_input.config(state='disable')
    
def limpiar():
    legajo.set('')
    alumno.set('')
    email.set('')
    calificacion.set('')
    escuela.set('Seleccionar')
    localidad.set('')
    provincia.set('')
    legajo_input.config(state='normal')

def crear():
    id_escuela = int(buscar_escuela(True)[0])
    datos = id_escuela, alumno.get(), calificacion.get(), email.get(), legajo.get()
    cur.execute('INSERT INTO alumnos (id_escuela, nombre, nota, email, legajo) VALUES (?,?,?,?,?)', datos)
    con.commit()
    messagebox.showinfo('Status', 'Alumno agregado')
    limpiar()
    
    

def actualiza():
    pass

def borrar():
    pass
    
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
bbddmenu.add_command(label="Conectar", command=conectar)
bbddmenu.add_command(label="Salir", command=salir)
barramenu.add_cascade(label="BBDD", menu=bbddmenu)

limpiarmenu = Menu(barramenu, tearoff=0)
limpiarmenu.add_command(label="Limpiar campos", command = limpiar)
barramenu.add_cascade(label='Limpiar', menu=limpiarmenu)

ayudamenu = Menu(barramenu, tearoff=0)
ayudamenu.add_command(label='Licencia', command=licencia)
ayudamenu.add_command(label='Acerca de..', command=acerca)
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

escuelas_lista = buscar_escuela(False)

#escuela_input = Entry(framecampos, textvariable=escuela)
#escuela_input.grid(row=4, column=2, padx=10, pady=10)
escuela_option = OptionMenu(framecampos, escuela, *escuelas_lista)
escuela_option.grid(row=4, column=2, padx=10, pady=10)

localidad_input = Entry(framecampos, textvariable=localidad, state='readonly')
localidad_input.grid(row=5, column=2, padx=10, pady=10)

provincia_input = Entry(framecampos, textvariable=provincia, state='readonly')
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

boton_crear = Button(framebotones, text='Crear', command = crear)
boton_crear.grid(row=0, column=0, padx=5, pady=10)

boton_leer = Button(framebotones, text='leer', command=leer)
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


