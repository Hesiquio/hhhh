# Este programa suma dos numeros
print("Calculadora")

sel=0
while(sel!=6):
	print(" ")
	print("1 Suma")
	print("2 Resta")
	print("6 Salir")
	sel=int(input("Ingrese el numero de la operacion que desea ejecutar: "))
	if sel == 1:
		print("Suma")
		a=int(input("Ingrese el numero 1: "))
		b=int(input("Ingrese el numero 2: "))
		suma=a+b
		print("El resultado de la suma es:", suma)

	elif sel==2:
		print("Resta")
		a=int(input("Ingrese el numero 1: "))
		b=int(input("Ingrese el numero 2: "))
		resta=a-b
		print("El resultado de la resta es:", resta)
	elif sel==6:
		print("Adios")
	else:
		print("Opcion no valida")