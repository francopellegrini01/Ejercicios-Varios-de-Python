import tkinter as tk
from PIL import ImageTk, Image
import os #no entiendo que importa esto

nominanombres = []
nominaapellidos = []
nominadni = []
legajos = []

contador = 0


def validaciondenumero(miparametro):
	if miparametro.isdigit() is False:

		etiqueta_datos.config(text="DNI Invalido", bg="black", fg="white",font=("Courier", 12))  #¿salida es una variable?
		etiqueta_datos.place(x=x_, y=y_ +350, width=700, height=50)#la posiciono
		miparametro = ""
		campo_DNI.delete(0, tk.END)
	return miparametro

def validaciondetexto(miparametro):
	if miparametro.isdigit() is True: #or nombre.isdigit() is True or apellido.isdigit() :

		etiqueta_datos.config(text="Ingreso numero, en campo texto", bg="black", fg="white",font=("Courier", 12))  #¿salida es una variable?
		etiqueta_datos.place(x=x_, y=y_ +350, width=700, height=50)#la posiciono
		miparametro = ""
		campo_nombre.delete(0, tk.END)
		campo_apellido.delete(0, tk.END)
	return miparametro

def agregar():
	global contador
	
	
	nombre = validaciondetexto(campo_nombre.get())
	if nombre == "":
		return
	nominanombres.append(nombre)

	apellido = validaciondetexto(campo_apellido.get())
	if apellido == "":
		return
	nominaapellidos.append(apellido)
	
	DNI = validaciondenumero(campo_DNI.get())
	if DNI == "":
		return
	nominadni.append(DNI)
	
	
	if (nombre == "" or apellido == "" or DNI == ""):
		salida=f"no ingreso los datos necesarios"
	else:
		
		contador+=1
		legajos.append(contador)
		salida=f"Se añadio a {nombre} {apellido}, con DNI N°: {DNI}\n a la Nómina de personal. Legajo N°: {contador}"
	
	etiqueta_datos.config(text=salida, bg="black", fg="white",font=("Courier", 12))  #¿salida es una variable?
	etiqueta_datos.place(x=x_, y=y_ +350, width=700, height=50)#la posiciono


def limpiar ():
	campo_apellido.delete(0, tk.END)
	campo_nombre.delete(0, tk.END)
	campo_DNI.delete(0, tk.END)

def salir ():
	exit ()


def Imprimirlista ():
	print ("Apellidos ingresados: ", nominaapellidos)
	print ("Nombres ingresados: ", nominanombres)
	print ("DNI ingresados: ", nominadni)
	print ("Legajos generados: ", legajos)
	
	return (legajos)
	etiqueta_datos.config((legajos), bg="black", fg="white",font=("Courier", 12))  #¿salida es una variable?
	etiqueta_datos.place(x=x_, y=y_ +300, width=700, height=50)#la posiciono
	return (etiqueta_datos)

x_=25
y_=75

miprimerventana = tk.Tk()

miprimerventana.title("Bienvenido al primer programa de pantallas graficas")

miprimerventana.geometry("800x600")

miprimerventana.config(bg = '#808080')







#programo la etiqueta del primer campo nombre
etiqueta_nombre = tk.Label(text="Ingresa tu nombre:")
etiqueta_nombre.config(bg="black", fg ="white", font = ("Calibri", 13))
etiqueta_nombre.place(x = x_, y = y_+25, width = 150, height = 25)

#programo el primer campo de la etiqueta campo nombre
campo_nombre = tk.Entry()
campo_nombre.place (x = x_+190, y = y_+25, width = 150, height = 25)




#programo la etiqueta apellido
etiqueta_apellido = tk.Label(text="Ingrese su apellido: ")
etiqueta_apellido.config(bg="black", fg="white", font = ("Calibri", 13))
etiqueta_apellido.place(x = x_, y = y_+75, width = 150, height = 25)

#programo el campo de la etiqueta apellido
campo_apellido = tk.Entry()
campo_apellido.place (x = x_+190, y = y_+75, width = 150, height =25)











#programo la etiqueta DNI
etiqueta_apellido = tk.Label(text="Ingrese su DNI: ")
etiqueta_apellido.config(bg="black", fg="white", font = ("Calibri", 13))
etiqueta_apellido.place(x = x_, y = y_+125, width = 150, height = 25)

#programo el campo de la etiqueta DNI
campo_DNI = tk.Entry()
campo_DNI.place (x = x_+190, y = y_+125, width = 150, height =25)







################ AGREGO LOS BOTONES ##############

#programo el boton añadir
botonAgregar = tk.Button(text = "Agregar", command = agregar) 
botonAgregar.place( x= x_, y = y_+200, width =150, height = 25) #ubico al boton


#programo el boton limpiar
botonLimpiar = tk.Button(text = "Limpiar", command = limpiar) 
botonLimpiar.place( x= x_+175, y = y_+200, width =150, height = 25) #ubico al boton


#programo el boton salir
botonSalir = tk.Button(text = "Salir", command = salir) 
botonSalir.place( x= x_+350, y = y_+200, width =150, height = 25) #ubico al boton



#programo el boton imprimir lista
botonImprimirlista = tk.Button(text = "Imprimir lista", command = Imprimirlista) 
botonImprimirlista.place( x= x_, y = y_+250, width =500, height = 25) #ubico al boton




# ~ #ACA CREO UNA ETIQUETA
etiqueta_datos = tk.Label(text="") #creo la etiqueta vacia
etiqueta_datos.config (bg = "red", fg = "white", font = ("Calibri",12)) #genero atributos #preguntar ariel esta linea. Ariel la hizo fondo blanco y etiqueta blanca, y los colores se solapan
# ~ etiqueta_datos.place (x = x_, y = y_+300, width = 600, height = 25) #posicion la etiqueta
#solo lo puedo resolver si comento la ubicacion







############### AGREGO UNA FOTO ##################
img = Image.open("RRHH-software.jpg")
img = img.resize((200, 100), Image.ANTIALIAS) #le digo el tamaño de pixeles que va a tener
RRHH = ImageTk.PhotoImage(img) #la guardo en el objeto RRHH
lab_im = tk.Label(image=RRHH)
lab_im.place(x=600, y= y_+25, width = 100, height = 100) 









miprimerventana.mainloop()

