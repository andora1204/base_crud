from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as tex_and_scroll
from datetime import datetime
import sqlite3

#####control de datos de usuarios#####################################
def nombres():
	nombres_completos=nombre_usuario.get()
	nombres_completos1=nombres_completos.title()
	if nombres_completos1.isdigit()==True or nombres_completos1=="":
		messagebox.showwarning("Advertencia",
		 "Problemas en el campo 'Nombres' parece que escribiste caracteres no validos, asegurese de no colocar numeros, no se debe dejar este campo vacio")
	else:
		return nombres_completos1

def apellidos():
	apellidos_completos=apellido_usuario.get()
	apellidos_completos1=apellidos_completos.title()
	if apellidos_completos1.isdigit()==True or apellidos_completos1=="":
		messagebox.showwarning("Advertencia",
		 "Problemas en el campo 'Apellidos' parece que escribiste caracteres no validos, asegurese de no colocar numeros, no se debe dejar este campo vacio")
	else:
		return apellidos_completos1

def cedula():
	if cedula_usuario.get().isdigit()==False or len(cedula_usuario.get())<7 or len(cedula_usuario.get())>8:
		messagebox.showwarning("Advertencia", """Problemas en el campo cedula pareceque escribiste caracteres no validos, asegurese de colocar numeros validosy asegurese de no colocar puntos ni comas, en caso de no poseer cedula escriba siete u ocho ceros (0000000)""")
	else:
		return cedula_usuario.get()

def email():
	email1= correo_usuario.get()
	correo = email1.lower()

	arroba= correo.count("@")

	lugar_arroba= correo.find("@")

	usuario= correo[:lugar_arroba]

	email= correo[lugar_arroba+1:]

	punto= email.find(".")

	extencion= email[punto:]

	cantidad_punto=extencion.count(".")
	if arroba!=1 or correo.find("@")==len(correo)-1 or correo.find("@")==0 or len(usuario)<8 or len(email)<8:

		messagebox.showwarning("Advertencia",
		 "Correo invalido, por favor verifique e intente de nuevo")

	elif cantidad_punto!=1 or len(extencion)>4  or extencion.find(".")==len(extencion)-1\
	 or extencion.find(".")==len(extencion)-2:

		messagebox.showwarning("Advertencia",
		 "Correo invalido, por favor verifique e intente de nuevo")
	else:
		return correo

def phone_cel():
	movilnet1 = "0416"
	movilnet2 = "0426"
	movistar1 = "0414"
	movistar2 = "0424"
	digitel = "0412"
	cantv = "0251"
	

	if var_option.get() == 1:
		phone = digitel + telefono_usuario.get()

	if var_option.get() == 2:
		phone = movistar1 + telefono_usuario.get()

	if var_option.get() == 3:
		phone = movistar2 + telefono_usuario.get()

	if var_option.get() == 4:
		phone = movilnet1 + telefono_usuario.get()

	if var_option.get() == 5:
		phone = movilnet2 + telefono_usuario.get()

	if var_option.get() == 6:
		phone = cantv + telefono_usuario.get()

	if var_option.get() == 0:
		messagebox.showwarning("Advertencia",
		 "Por favor elija codigo telefonico")

	if telefono_usuario.get() == 0 or len(telefono_usuario.get()) <= 6\
	 or len(telefono_usuario.get()) > 7 or telefono_usuario.get().isdigit() == False:
		messagebox.showwarning("Advertencia",
		 "telefono invalido, por favor verifique e intente de nuevo")
	else:
		return phone

	
	return phone

def genero():

	if var_option1.get() == 7:
		sexualidad = "Masculino"

	if var_option1.get() == 8:
		sexualidad = "Femenino"

	if var_option1.get() == 0:
		messagebox.showwarning("Advertencia",
		 "Por favor elija su Genero")

	
	return sexualidad

def fecha_nacimiento():

	
	try:
		
		formato_nac = datetime.strptime(fecha_usuario.get(), "%d/%m/%Y")	
		return formato_nac
	except ValueError:

		return False
		

		
			


def nacimiento_str():

	try:
	

		fecha_str = fecha_nacimiento().strftime("%d/%m/%Y")
		return fecha_str

	except:
		return False
		


	

def edad():


	hoy_es = datetime.now()

	anio_nac = fecha_nacimiento().year
	mes_nac = fecha_nacimiento().month
	dia_nac = fecha_nacimiento().day

	year_today = hoy_es.year
	month_today = hoy_es.month
	day_today = hoy_es.day

	edad_promedio = year_today - anio_nac

	if month_today < mes_nac or day_today < dia_nac:
		edad = edad_promedio - 1
	elif edad_promedio <= 2 or edad_promedio > 100:
		messagebox.showwarning("Advertencia",
			"Por favor verifique su fecha")
	elif month_today == mes_nac and day_today == dia_nac:
		edad = edad_promedio
		messagebox.showinfo("Felicidades!", f"hoy esta de cumpleaños Feliz Cumpleaños!! {edad_promedio}")
			

	else:
		edad = edad_promedio

	return edad



def fecha_de_hoy():

	hoy_es = datetime.now()
	
	formato_fecha = datetime.strftime(hoy_es, "%d/%m/%Y")
	return formato_fecha

def fecha_actualizacion():
	hoy_es = datetime.now()
	
	formato_fecha = datetime.strftime(hoy_es, "%d/%m/%Y")
	return formato_fecha



##Base de datos SQL######################################################
def conectar():
	mi_conexion=sqlite3.connect("Datos_Completos")
	mi_cursor=mi_conexion.cursor()

	mi_cursor.execute("""CREATE TABLE USUARIOS(

		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		NOMBRES VARCHAR(30),
		APELLIDOS VARCHAR(30),
		CEDULA INTEGER(8),
		FECHA NACIMIENTO VARCHAR(10),
		EDAD INTEGER (3),
		CORREO VARCHAR(20),
		DIRECCION VARCHAR(50),
		TELEFONO VARCHAR(7),
		SEXO VARCHAR(15),
		COMENTARIOS VARCHAR(250),
		FECHA_INGRESO,
		FECHA_ACTUALIZACION

		)""")
	mi_conexion.commit()
	mi_conexion.close()




def insertar():

	mi_conexion=sqlite3.connect("Datos_Completos")
	mi_cursor=mi_conexion.cursor()

	if nacimiento_str() == False:
		messagebox.showwarning("Advertencia",
		"coloque bien el formato especificado dd/mm/aaaa")
	else:

		lista_usuarios=[]
		lista_usuarios.append(nombres())
		lista_usuarios.append(apellidos())		
		lista_usuarios.append(cedula())
		lista_usuarios.append(nacimiento_str())
		lista_usuarios.append(edad())
		lista_usuarios.append(email())
		lista_usuarios.append(direccion_usuario.get())	
		lista_usuarios.append(phone_cel())
		lista_usuarios.append(genero())
		lista_usuarios.append(campo_comentarios.get("1.0", END))
		lista_usuarios.append(fecha_de_hoy())
		lista_usuarios.append(fecha_actualizacion())

		mi_cursor.execute("INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?)",lista_usuarios)

			

		mi_conexion.commit()
		mi_conexion.close()


def leer():
	mi_conexion=sqlite3.connect("Datos_Completos")
	mi_cursor=mi_conexion.cursor()
	campo_comentarios.delete(1.0, END)

	numero_ID = int(ID_usuario.get())

	mi_cursor.execute(f"SELECT * FROM USUARIOS WHERE ID={numero_ID}")

	lectura_tabla = mi_cursor.fetchall()

	for i in lectura_tabla:
		nombre_usuario.set(i[1])
		apellido_usuario.set(i[2])
		cedula_usuario.set(i[3])
		fecha_usuario.set(i[4])
		correo_usuario.set(i[6])
		direccion_usuario.set(i[7])
		# el numero de telefono de la base es i[8], voy a dividirlo en prefijo y sufijo por lo tanto
		telf_base = i[8]
		prefijo = telf_base[0:4]
		sufijo = telf_base[4:11]
		if prefijo == "0412":
			var_option.set(1)
		if prefijo == "0414":
			var_option.set(2)
		if prefijo == "0424":
			var_option.set(3)
		if prefijo == "0416":
			var_option.set(4)
		if prefijo == "0426":
			var_option.set(5)
		if prefijo == "0251":
			var_option.set(6)
		telefono_usuario.set(sufijo)
		if i[9]=="Masculino":
			var_option1.set(7)
		else:
			var_option1.set(8)

		campo_comentarios.insert(1.0,i[10])
		messagebox.showinfo("Edad!", f"La edad de esta persona es  {i[5]} e ingresó al sistema el {i[11]}, el sistema no se ha actualizado desde {i[12]}")



	mi_conexion.commit()
	mi_conexion.close()




#Interfaz Grafica##########################################################


root=Tk()
root.title("Datos de Usuarios")



######Barra Menu#######################################################################

menu_bar=Menu(root)
root.config(menu=menu_bar)

sub_BBDD=Menu(menu_bar, tearoff=0)
sub_BBDD.add_command(label="Conectar", command=conectar)
sub_BBDD.add_command(label="Insertar", command=insertar)
sub_BBDD.add_separator()
sub_BBDD.add_command(label="Salir")

sub_Borrar=Menu(menu_bar, tearoff=0)
sub_Borrar.add_command(label="Borrar Campos")

sub_CRUD=Menu(menu_bar, tearoff=0)
sub_CRUD.add_command(label="Crear")
sub_CRUD.add_command(label="Leer")
sub_CRUD.add_command(label="Actualizar")
sub_CRUD.add_command(label="Borrar")

sub_ayuda=Menu(menu_bar, tearoff=0)
sub_ayuda.add_command(label="Información")
sub_ayuda.add_command(label="Ayuda")


menu_bar.add_cascade(label="BBDD", menu=sub_BBDD)
menu_bar.add_cascade(label="Borrar", menu=sub_Borrar)
menu_bar.add_cascade(label="CRUD", menu=sub_CRUD)
menu_bar.add_cascade(label="Ayuda", menu=sub_ayuda)
################################################################################################
##cuadros y textos a escribir por usurios#######################################################
my_frame=Frame(root)
my_frame.pack()

etiqueta_ID=Label(my_frame, text="ID:")
etiqueta_ID.grid(row=0, column=0)



etiqueta_nombres=Label(my_frame, text="Nombres:")
etiqueta_nombres.grid(row=1, column=0)

etiqueta_apellidos=Label(my_frame, text="Apellidos:")
etiqueta_apellidos.grid(row=2, column=0)

etiqueta_Cedula=Label(my_frame, text="Cedula:")
etiqueta_Cedula.grid(row=3, column=0)

etiqueta_fecha=Label(my_frame, text="Fecha de Nacimiento (dd/mm/aaaa):")
etiqueta_fecha.grid(row=4, column=0)

etiqueta_correo=Label(my_frame, text="Correo Electronico:")
etiqueta_correo.grid(row=5, column=0)

etiqueta_direccion=Label(my_frame, text="Dirección:")
etiqueta_direccion.grid(row=6, column=0)

etiqueta_telefono=Label(my_frame, text="Telefono:")
etiqueta_telefono.grid(row=10, column=0)

etiqueta_sexo=Label(my_frame, text="Genero:").grid(columnspan=2)

etiqueta_comentarios=Label(my_frame, text="Comentarios:")
etiqueta_comentarios.grid(row=13, column=0)


ID_usuario=StringVar()
campo_ID=Entry(my_frame, textvariable=ID_usuario)
campo_ID.grid(row=0, column=1)

nombre_usuario=StringVar()
campo_nombres=Entry(my_frame, textvariable=nombre_usuario)
campo_nombres.grid(row=1, column=1)


apellido_usuario=StringVar()
campo_apellidos=Entry(my_frame, textvariable=apellido_usuario)
campo_apellidos.grid(row=2, column=1)

cedula_usuario=StringVar()
campo_cedula=Entry(my_frame, textvariable=cedula_usuario)
campo_cedula.grid(row=3, column=1)

fecha_usuario=StringVar()
campo_fecha=Entry(my_frame, textvariable=fecha_usuario)
campo_fecha.grid(row=4, column=1)

correo_usuario=StringVar()
campo_correo=Entry(my_frame, textvariable=correo_usuario)
campo_correo.grid(row=5, column=1)

direccion_usuario=StringVar()
campo_direccion=Entry(my_frame, textvariable=direccion_usuario)
campo_direccion.grid(row=6, column=1)

var_option=IntVar()
variable_radiot=Radiobutton(my_frame, text="0412", variable=var_option, value=1)
variable_radiot.grid(row=7, column=0)

variable_radiot=Radiobutton(my_frame, text="0414", variable=var_option, value=2)
variable_radiot.grid(row=7, column=1)

variable_radiot=Radiobutton(my_frame, text="0424", variable=var_option, value=3)
variable_radiot.grid(row=8, column=0)

variable_radiot=Radiobutton(my_frame, text="0416", variable=var_option, value=4)
variable_radiot.grid(row=8, column=1)

variable_radiot=Radiobutton(my_frame, text="0426", variable=var_option, value=5)
variable_radiot.grid(row=9, column=0)

variable_radiot=Radiobutton(my_frame, text="0251", variable=var_option, value=6)
variable_radiot.grid(row=9, column=1)

telefono_usuario=StringVar()
campo_telefono=Entry(my_frame, textvariable=telefono_usuario)
campo_telefono.grid(row=10, column=1)



var_option1=IntVar()
variable_radio=Radiobutton(my_frame, text="Masculino", variable=var_option1, value=7)
variable_radio.grid(row=12, column=0)

variable_radio=Radiobutton(my_frame, text="Femenino", variable=var_option1, value=8)
variable_radio.grid(row=12, column=1)


campo_comentarios=tex_and_scroll.ScrolledText(my_frame, width=20, height=5, padx=0, pady=10)
campo_comentarios.grid(row=13, column=1)


my_frame2=Frame(root)
my_frame2.pack()

primer_boton=Button(my_frame2, text="Create")
primer_boton.grid(row=0, column=0, padx=5, pady=10)

segundo_boton=Button(my_frame2, text="Read", command=leer)
segundo_boton.grid(row=0, column=1, padx=5, pady=10)

tercer_boton=Button(my_frame2, text="Update")
tercer_boton.grid(row=0, column=2, padx=5, pady=10)

cuarto_boton=Button(my_frame2, text="Delete")
cuarto_boton.grid(row=0, column=3, padx=5, pady=10)

quinto_boton=Button(my_frame2, text="Insert")
quinto_boton.grid(row=0, column=4, padx=5, pady=10)


root.mainloop()



