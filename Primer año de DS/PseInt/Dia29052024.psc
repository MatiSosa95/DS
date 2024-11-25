Algoritmo Dia29052024
	contadorDeNumerosEnteros;
FinAlgoritmo

Funcion contadorDeNumerosEnteros
	Definir num, contador Como Entero
	contador=0; 
	Escribir "Ingrese un numero positivo";
	leer num; 
	Mientras num<>0 Hacer
		si num<0 Entonces
			Escribir "Ingresó un numero negativo";
		SiNo
			contador=contador+1;
		FinSi
		Escribir "Ingrese un numero positivo";
		leer num;
	FinMientras
	Escribir "La cantidad de numeros positivos que ingresó es de ", contador;  
FinFuncion


	