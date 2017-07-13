# Este programa suma dos numeros
print("Calculadora")

sel=99
while(sel!=0):
	print(" ")
	print("Menu de Opciones: ")
	print("1 Suma")
	print("2 Resta")
	print("3 Multiplicacion")
	print("4 Division")
	print("5 Verificacion")
	#Linea de codigo modificada por terceros lol
	print("0 Salir")
	print(" ")
	
	sel=int(input("Ingrese el numero de la opcion que desea ejecutar: "))
	
	if sel == 1:
		print(" ")
		print("Ha elegido la opcion Suma")
		a=int(input("Ingrese el numero 1: "))
		b=int(input("Ingrese el numero 2: "))
		suma=a+b
		print("El resultado de la suma es:", suma)
		print(" ")

	elif sel==2:
		print(" ")
		print("Ha elegido la opcion Resta")
		a=int(input("Ingrese el numero 1: "))
		b=int(input("Ingrese el numero 2: "))
		resta=a-b
		print("El resultado de la resta es:", resta)
		print(" ")
		
	elif sel==3:
		print(" ")
		print("Ha elegido la opcion Multiplicacion")
		a=int(input("Ingrese el numero 1: "))
		b=int(input("Ingrese el numero 2: "))
		mult=a*b
		print("El resultado de la multiplicacion es:", mult)
		print(" ")
		
	elif sel==4:
		print(" ")
		print("Ha elegido la opcion Division")
		a=int(input("Ingrese el numero 1: "))
		b=int(input("Ingrese el numero 2: "))
		div=a/b
		print("El resultado de la divicion es:", div)
		print(" ")
		
	elif sel==0:
		print(" ")
		print("Adios")
	
	elif sel==5:
		print("Verificado por Karely, Karla y Avila")
	else:
		print("Opcion no valida")
		