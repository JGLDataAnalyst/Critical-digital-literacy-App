#1. CELapp INICI CELappp + INICI DE SESSIÓ
from tkinter import *
import os
from tkinter import messagebox as error
def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    ventana_principal.geometry("1000x550")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("CELapp Inici de Sessió")#TITULO DE LA VENTANA
    imagen=PhotoImage(file="uab.png")
    fondo=Label(ventana_principal,image=imagen).place(x=-120,y=60)
    Label(bg="black", width="300", height="2").pack()
    Label(text="").pack()
    Button(text="Accedir", height="2", width="30", bg=pestas_color, command=login).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrar-se", height="2", width="30", bg=pestas_color, command=registro).pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    ventana_principal.mainloop()

def registro(): 
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registre de dades CELapp")
    ventana_registro.geometry("400x225")
 
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "nombre_usuario"
    clave = StringVar() #DECLARAMOS "sytring" COMO TIPO DE DATO PARA "clave"
 
    Label(ventana_registro, bg="black", width="150", height="1").pack()
    Label(ventana_registro, text="").pack()
    etiqueta_nombre = Label(ventana_registro, text="Nom d'usuari:")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Contrasenya:")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_clave.pack()
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrar-se", width=10, height=1, bg="Black", command = registro_usuario).pack() #BOTÓN "Registrarse"

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Accedeix al compte CELapp")
    ventana_login.geometry("400x250")
    Label(ventana_login, bg="black", width="150", height="1").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nom d'usuari:").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña:").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Accedeix", width=10, height=1, command = verifica_login).pack()

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
 
    lista_archivos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if usuario1 in lista_archivos:
        archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        if clave1 in verifica:
            exito_login() #...EJECUTAR FUNCIÓN "exito_login()"
        #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
        else:
            no_clave() #...EJECUTAR "no_clave()"
    
    else:
        no_usuario() #..EJECUTA "no_usuario()".

 
def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("ÈXIT")
    ventana_exito.geometry("250x50")
    Label(ventana_exito, text="Inici de sessió finalitzat amb èxit", bg="green").pack()
    Button(ventana_exito, text="D'acord", command=borrar_exito_login).pack()
 
def no_clave():
    error.showwarning("CELappAlert","Accès denegat.\nMotiu: Contrasenya incorrecte.")
 
def no_usuario():
    error.showwarning("CELappAlert","Accès denegat.\nMotiu: Usurari incorrecte.")

def borrar_exito_login():
    ventana_exito.destroy()
 
 
def borrar_no_clave():
    ventana_no_clave.destroy()
 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()
 
def registro_usuario():
 
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
 
    file = open(usuario_info, "w") #CREACION DE ARCHIVO CON "nombre" y "clave"
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
 
    Label(ventana_registro, text="Registre realitzat amb èxit", fg="green", font=("calibri", 11)).pack()
  
ventana_inicio()  #EJECUCIÓN DE LA VENTANA DE INICIO.
