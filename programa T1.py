import re
#patron = re.compile('a[3-5]+')# coincide con una letra, seguida de al menos 1 dígito entre 3 y 5
#print( input("Introduce un texto") );
import re

archivo=open("datosA.txt","r")
mensaje=archivo.read()



p1 = re.compile('(int |long |byte |short )')
p2 = re.compile('(double |float )')
p3 = re.compile('(String )')
p4 = re.compile('(boolean )')



if p1.findall(mensaje)!=[]:#condicion para encontrar el primer patron (int, long,byte,short)
	patron = re.compile('((int |long |byte |short )([A-Za-z]+\w?\=\-?(\d{1,7})((\+|\-|\*|\/)\d{1,7})?\;))')# expresion regular
	if patron.findall(mensaje)!=[]:#condicion para encontrar la expresion regular
		print("asignacion entera exitosa: "+str(patron.findall(mensaje)))#imprime exitoso en caso de ser correcto
	else:
		print("error en la asignacion de una variable entera")#mensaje en caso de ser erroneo
	archivo.close()
elif p2.findall(mensaje)!=[]:#condicion para encontrar el primer patron (double,float)
#variable real
	patron = re.compile('((double |float )([A-Za-z]+\w?\=\-?\d{1,7}\.\d{1,7}f?((\+|\-|\*|\/)\d{1,7}\.\d{1,7}f?)?\;))')# expresion regular
	if patron.findall(mensaje)!=[]:#condicion para encontrar la expresion regular
		print("asignacion real exitosa: "+str(patron.findall(mensaje)))#imprime exitoso en caso de ser correcto
	else:
		print("error en la asignacion de una variable real")#mensaje en caso de ser erroneo
	archivo.close()
elif p3.findall(mensaje)!=[]:#condicion para encontrar el primer patron (String)
#variable de cadena
	patron = re.compile('(String [A-Za-z]+\w?\=\"(\w(.+)?)?\"(\+\"(\w(.+)?)?\")?\;)')# expresion regular
	if patron.findall(mensaje)!=[]:#condicion para encontrar la expresion regular
		print("asignacion de cadena exitosa: "+str(patron.findall(mensaje)))#imprime exitoso en caso de ser correcto
	else:
		print("error en la asignacion de una variable de cadena")#mensaje en caso de ser erroneo
	archivo.close()
#variable de boolean
elif p4.findall(mensaje)!=[]:#condicion para encontrar el primer patron (boolean)
	patron = re.compile('(boolean [A-Za-z]+\w?\=(\-?\d{1,7}(\.\d{1,7})?(\<|\>|\=\=|\<\=|\>\=)\d{1,7}(\.\d{1,7})?|true|false)\;)')# expresion regular
	if patron.findall(mensaje)!=[]:#condicion para encontrar la expresion regular
		print("asignacion logica exitosa: "+str(patron.findall(mensaje)))#imprime exitoso en caso de ser correcto 
	else:
		print("error en la asignacion de una variable logica")#mensaje en caso de ser erroneo
	archivo.close()
	

#antonio contreras collo
#felipe balam canul
#diana noh tun
#gregorio poot cupul
#
