#coded by Jey Zeta
import sys, os, webbrowser, platform, subprocess, time

import webbrowser

def menu():
	if os.name == 'nt':
            os.system('cls')
	else:
            os.system('clear')






	print ('''
\033[1;31m __          ___          _____    ___  _____            _
\033[1;31m \ \        / / |        |_   _|  |__ \|  __ \          (_)
\033[1;34m  \ \  /\  / /| |__   ___  | |  ___  ) | |  | | _____  ___ _ __   __ _
\033[1;34m   \ \/  \/ / | '_ \ / _ \ | | / __|/ /| |  | |/ _ \ \/ / | '_ \ / _` |
\033[1;34m    \  /\  /  | | | | (_) || |_\__ \_| | |__| | (_) >  <| | | | | (_| |
\033[1;31m     \/  \/   |_| |_|\___/_____|___(_) |_____/ \___/_/\_\_|_| |_|\__, |
                                                                  __/ |
                                                                 |___/

					  \033[1;31mHacking Live\033[1;m
			  \033[1;34mHecho por:\033[1;m Victor Bancayan & Kelvin Parra
  				       \033[1;35mVersion: Beta 1.0
					   	\033[0;m(EDITED BY WHOAMI)

			''')

	print ('''
\033[1;32m 1. Pipl 	 \033[1;32m 7. Sis            \033[1;32m 13. Censo           \033[1;32m19. Sanciones   \033[1;32m 25. Direccion
\033[1;32m 2. Dni	 	 \033[1;32m 8. FecNac         \033[1;32m 14. EstadoDoc    \033[1;32m   20. Sat 	 \033[1;32m 26. SkypeIp
\033[1;32m 3. EstCiv    	 \033[1;32m 9. Credito       \033[1;32m  15. BuscarDatos  \033[1;32m   21. Runt  	 \033[1;32m 27. Multas
\033[1;32m 4. Operdora    \033[1;32m 10. Sentinel       \033[1;32m 16. Certificados   \033[1;32m 22. Libreta \033[1;32m     28. Username
\033[1;32m 5. Ruc       	\033[1;32m 11. ExifData       \033[1;32m 17. Licencia  	 \033[1;32m23. StalkScan  \033[1;32m  29. About
\033[1;32m 6. Tinfoleak   \033[1;32m 12. Acreditacion   \033[1;32m 18. Curp          \033[1;32m  24. Colegiados  \033[1;32m 30. Exit

\033[0;m IPInfo:\t   			\033[0;m Persona:\t\t	\033[0;m Social:		\033[0;mHelp
\033[1;34m 1. IpLocation\t		\033[1;34m 1. ConsultaPorNombre(CR)		\033[1;34m 1. PerfilFB  \t\t1.Usage
\033[1;34m 2. IPInfo\t   		\033[1;34m 2. ConsultaVehiculo(CR)		\033[1;34m 2. PageFB
\033[1;34m 3. Whois			\033[1;34m 3. ConsultaDNI(CR)			\033[1;34m 3. LugaresFB
\033[1;34m 4. Traceroute								\033[1;34m 4. Twitter
									\033[1;34m 5. PerfilIG

		''')

	d = input("\033[1;30m Doxing > ")


	if d == "1":
		webbrowser.open('https://pipl.com/')

		menu()
	elif d == "2":
		webbrowser.open('http://www.consultadni.info/')
		menu()
	elif d == "3":
		webbrowser.open('https://cel.reniec.gob.pe/valreg/valreg.do')
		menu()
	elif d == "4":
		webbrowser.open('http://www.deperu.com/celulares/')
		menu()
	elif d == "5":
		webbrowser.open('http://www.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias')
		menu()
	elif d == "6":
		webbrowser.open('https://tinfoleak.com/')
		menu()
	elif d == "7":
		webbrowser.open('http://app.sis.gob.pe/SisConsultaEnLinea/Consulta/frmConsultaEnLinea.aspx')
		menu()
	elif d == "8":
		webbrowser.open('https://www.reniec.gob.pe/concer/concer.do')
		menu()
	elif d == "9":
		webbrowser.open('https://www.icetex.gov.co/portalacces/tradicional/solicitar/cptConsultarEstado.asp?origen=portal')
		menu()
	elif d == "10":
		webbrowser.open('https://misentinel.sentinelperu.com/misentinel/misentinel.aspx')
		menu()
	elif d == "11":
		webbrowser.open('http://exifdata.com')
		menu()
	elif d == "12":
		webbrowser.open('http://ww4.essalud.gob.pe:7777/acredita/index.jsp')
		menu()
	elif d == "13":
		webbrowser.open('https://wsp.registraduria.gov.co/censo/_censoResultado.php')
		menu()
	elif d == "14":
		webbrowser.open('https://wsp.registraduria.gov.co/estadodocs/')
		menu()
	elif d == "15":
		webbrowser.open('http://buscardatos.com/')
		menu()
	elif d == "16":
		webbrowser.open('http://certificados.sena.edu.co/')
		menu()
	elif d == "17":
		webbrowser.open('http://web.mintransporte.gov.co/Consultas/transito/Consulta23122010.htm')
		menu()
	elif d == "18":
		webbrowser.open('https://consultas.curp.gob.mx/')
		menu()
	elif d == "19":
		webbrowser.open('https://consulta.simit.org.co/Simit/index.html')
		menu()
	elif d == "20":
		webbrowser.open('https://www.sat.gob.pe/Websitev9')
		menu()
	elif d == "21":
		webbrowser.open('https://www.runt.com.co/consultaCiudadana/#/consultaPersona')
		menu()
	elif d == "22":
		webbrowser.open('https://www.libretamilitar.mil.co/Modules/Consult/MilitarySituation')
		menu()
	elif d == "23":
		webbrowser.open('https://stalkscan.com/')
		menu()
	elif d == "24":
		webbrowser.open('http://www.cipica.com/buscolegiado/buscolegiado.php')
		menu()
	elif d == "25":
		webbrowser.open('http://www.midis.gob.pe/padron/')
		menu()
	elif d == "26":
		webbrowser.open('http://mostwantedhf.info/')
		menu()
	elif d == "27":
		webbrowser.open('http://aplicaciones007.jne.gob.pe/multas/')
		menu()
	elif d == "28":
		webbrowser.open('https://namechk.com/')
		menu()
	elif d == "29":
		webbrowser.open('https://www.facebook.com/HackingEnVivo/')
		menu()
	elif d == "30":
		sys.exit()

	elif d == "ipinfo":
		while d == "ipinfo":
			x = input("\033[1;30m IPInfo > ")
			if x == "1":
				webbrowser.open('https://www.iplocation.net')


			elif x == "2":
				webbrowser.open('https://www.ip2location.com')


			elif x == "3":
				webbrowser.open('https://domainbigdata.com/')


			elif x == "back":
				menu()

			elif x == "4":
				if os.name == "nt":
					w = input ("Digite la direccion IP: ")
					os.system ("tracert " + w)
					input()

				else:
					l = input ("Digite la direccion IP: ")
					os.system("traceroute " + l)
					input()



			else:
				print("Digite un valor valido")
				input()



	elif d == "persona":
		while d == "persona":
			a = input ("\033[1;30m Persona >")
			if a == "1":
				webbrowser.open('https://www.consulta.tse.go.cr/consulta_persona/consulta_nombres.aspx')

			elif a == "2":
				webbrowser.open('http://marchamo.ins-cr.com/Marchamo/Marchamo/frmConsultaMarchamo.aspx')

			elif a == "3":
				webbrowser.open('https://www.consulta.tse.go.cr/consulta_persona/consulta_cedula.aspx')


			elif a == "back":
				menu()

			else:
				print("Digite un valor valido")
				input()

	elif d == "social":
		while d == "social":
			b = input ("\033[1;30m Social > ")
			if b == "1":
				webbrowser.open('https://www.facebook.com/directory/people/')


			elif b == "2":
					webbrowser.open('https://www.facebook.com/directory/pages/')

			elif b == "3":
					webbrowser.open('https://www.facebook.com/directory/places/')

			elif b == "4":
					webbrowser.open('https://mobile.twitter.com/i/directory/profiles/')

			elif b == "5":
					webbrowser.open('https://www.instagram.com/about/directory/')

			elif b == "back":
				menu()

			else:
				print("Digite un valor valido")



	elif d == "help":
		print ("Usage:\nEscribe: ipinfo, persona o social para utilizar un sub menu.\nPresiona cualquier tecla para continuar")
		input()
		menu()



	else:
		print("Error no se encontro " + d)
		input()
		menu()


menu()
