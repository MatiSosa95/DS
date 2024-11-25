Algoritmo Factorial
	definir num,i,j, total, n Como Entero

	Escribir "Ingrese cantidad de números a los cuales desea calcular su factorial : "
	leer n
	
	Para i<-1 Hasta n Con Paso 1 Hacer
		Escribir "Ingrese el numero positivo que quiera calcular el factorial"
		leer num
		total=1; 
		si num>0 Entonces
			Para j<-1 Hasta num Con Paso 1 Hacer
				total= j*total;
			Fin Para
		SiNo
			
			Escribir "Ingresó un numero erroneo";
		FinSi
		escribir "el factorial del número ", num, " es:", total;
	Fin Para
	
FinAlgoritmo
