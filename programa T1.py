import re
#patron = re.compile('a[3-5]+')# coincide con una letra, seguida de al menos 1 dígito entre 3 y 5
#print( input("Introduce un texto") );
archivo=open('datosA.txt','r')
#print("el texto es: "+archivo.read())
mensaje=archivo.read()


print("ingresa un una opcion")
print("1: variable entera")
print("2: variable real")
print("3: variable de cadena")
print("4: variable logica")
numero = int(input())

if numero==1:
	#variable entera
	patron = re.compile('((int |long |byte |short )[A-Za-z]+\w?\=\-?(\d{1,7})((\+|\-|\*|\/)\d{1,7})?\;)')
	print (patron.findall(mensaje))
	if patron.findall(mensaje)!=[]:
		print("asignacion entera exitosa")
	else:
		print("error en la asignacion de una variable entera")
	archivo.close()


if numero==2:
	#variable real
	patron = re.compile('((double |float )([A-Za-z]+\w?\=\-?\d{1,7}\.\d{1,7}f?((\+|\-|\*|\/)\d{1,7}\.\d{1,7}f?)?\;))')
	print (patron.findall(mensaje))
	if patron.findall(mensaje)!=[]:
		print("asignacion real exitosa")
	else:
		print("error en la asignacion de una variable real")
	archivo.close()

if numero==3:
	#variable de cadena
	patron = re.compile('(String [A-Za-z]+\w?\=\"(\w(.+)?)?\"(\+\"(\w(.+)?)?\")?\;)')
	print (patron.findall(mensaje))
	if patron.findall(mensaje)!=[]:
		print("asignacion de cadena exitosa")
	else:
		print("error en la asignacion de una variable de cadena")
	archivo.close()

if numero==4:
	#variable logica 
	print( "VALIDACION DE DATOS LOGICOS 10 + 5 = 10")
	logico = bool(10 + 5 == 15)
	print (logico)

	print( "Erros de asignacion de datos logicos")
	logico = bool(2 >" hola ")
	print (logico)

