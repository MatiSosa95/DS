Algoritmo MayorPoblacion

		Definir i,j, numDepartamentos, numCiudades, poblacion, mPoblacion Como Entero
		Definir dptoMayorPoblacion, ciudadMayorPoblacion, DptoActual, ciudadActual Como Caracter
		
		Escribir "Ingrese la cantidad de departamentos que desea recorrer: "
		Leer numDepartamentos
		
		mPoblacion = 0
		dptoMayorPoblacion =""
		ciudadMayorPoblacion = ""
		
		Para i <- 1 Hasta numDepartamentos Con Paso 1 Hacer
			Escribir "Ingrese el nombre del departamento ", i, ": "
			Leer DptoActual
			
			Escribir "Ingrese la cantidad de ciudades en ", DptoActual, ": "
			Leer numCiudades
			
			Para j <- 1 Hasta numCiudades Con Paso 1 Hacer
				Escribir "Ingrese el nombre de la ciudad ", j, " de ", DptoActual, ": "
				Leer ciudadActual
				
				Escribir "Ingrese la cantidad de habitantes de ", ciudadActual, ": "
				Leer poblacion
				
				Si poblacion > mPoblacion Entonces
					mPoblacion = poblacion
					dptoMayorPoblacion = DptoActual
					ciudadMayorPoblacion = ciudadActual
				FinSi
			FinPara
		FinPara
		
		Escribir "La ciudad con mayor población es ", ciudadMayorPoblacion, " en el departamento ", dptoMayorPoblacion, " con una población de ", mPoblacion, " habitantes."


FinAlgoritmo
