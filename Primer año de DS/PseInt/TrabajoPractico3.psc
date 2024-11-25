Algoritmo TrabajoPractico3
	Ejercicio9 
FinAlgoritmo

Funcion Ejercicio1
	Definir n,i, resultado Como Entero
	Repetir
		Escribir "Ingrese el numero que desee saber la tabla de multiplicar"; 
		Leer n; 
	Mientras Que n<0
	Para i<-0 Hasta 10 Con Paso 1 Hacer
		resultado= n*i; 
		Escribir "El resultado de ", n, " x ", i, " = ", resultado; 
	Fin Para
FinFuncion

Funcion Ejercicio2
	Definir CapitalAInvertir, capitalGanado,interes,i Como Real; 
	Definir años Como entero; 
	capitalGanado=0;
	Escribir "Ingrese la cantidad que quiere invertir"; 
	Leer CapitalAInvertir; 
	Escribir "Ingrese el interes que desea ganar por año"; 
	Leer interes; 
	interes= interes/100; 
	Escribir "Ingrese la cantidad de años, en numeros enteros, que desea invertir"; 
	leer años; 
	
	Para i<-1 Hasta años Con Paso 1 Hacer
		capitalGanado= (CapitalAInvertir*interes); 
		CapitalAInvertir=capitalGanado+CapitalAInvertir;
		Escribir "El capital ganado en ", i, " años. Es de ", capitalGanado, ". Y el total ganado es de: ", CapitalAInvertir;
	Fin Para
	 
	
FinFuncion

Funcion Ejercicio3Mientras
	//Realice un programa que calcule la cantidad de nros ingresados y visualice la suma, promedio, el valor 
	//máximo, el valor mínimo de n números positivos ingresados por teclado. Pruebe las 3 versiones de 
	//repeticiones o bucles, usando el bucle "Mientras" y otra con "Hacer - Mientras Que" y otra usando el 
	//para. ¿Cuál le parece el mas conveniente? 
	//SE USA EL MIENTRAS
	
	Definir cantidad, n Como Entero; 
	Definir suma, max, min, prom Como Real; 
	cantidad=0; 
	suma=0; 
	max=0; 
	Escribir "Ingrese un numero entero positivo. Ingrese un 0 o un negativo para terminar"; 
	Leer n;
	min=n; 
	
	Mientras n>0
		suma=suma+n; ; 
		cantidad= cantidad+1; 
		
		si max<n Entonces
			max= n; 
		FinSi
		
		si min>n Entonces
			min= n; 
		FinSi
		
		Escribir "Ingrese un numero entero positivo. Ingrese un 0 o un negativo para terminar"; 
		Leer n; 
	FinMientras
	
	prom= suma/cantidad; 
	
	Escribir "La suma de todos los numeros ingresados es: ", suma; 
	Escribir "El promedio de la suma de todos los numeros ingresados es: ", prom; 
	Escribir "El valor maximo ingresado es: ", max; 
	Escribir "El valor minimo ingresado es: ", min; 
FinFuncion

Funcion Ejercicio3HacerMientras
	Definir cantidad, n Como Entero; 
	Definir suma, max, min, prom Como Real; 
	cantidad=0; 
	suma=0; 
	max=0;  
	
	Repetir
		Escribir "Ingrese un numero entero positivo. Ingrese un 0 o un negativo para terminar"; 
		Leer n;
		min=n; 
		suma=suma+n; 
		cantidad= cantidad+1; 
		
		si max<n Entonces
			max= n; 
		FinSi
		
		si min>n Entonces
			min= n; 
		FinSi
	Mientras Que n>0
	prom= suma/cantidad; 
	Escribir "La suma de todos los numeros ingresados es: ", suma; 
	Escribir "El promedio de la suma de todos los numeros ingresados es: ", prom; 
	Escribir "El valor maximo ingresado es: ", max; 
	Escribir "El valor minimo ingresado es: ", min; 
	
FinFuncion

funcion Ejercicio3Para
	Definir n, i, suma, cantidadDeIteraciones, max, min,num Como Entero
	Definir  prom como real; 
	suma=0; 
	Escribir "Ingrese un numero";
	leer num; 
	min= num; 
	max=num;
	Escribir "Ingrese la cantidad de numeros que desea sumar"
	Leer cantidadDeIteraciones; 
	
	Para i<-1 Hasta cantidadDeIteraciones Con Paso 1 Hacer
		Escribir "Ingrese un numero entero positivo"
		Leer n; 
		
		si n>0 Entonces
			suma=suma+n; 
			
			
			si max<n Entonces
				max= n; 
			FinSi
			
			si min>n Entonces
				min= n; 
			FinSi
			
		FinSi
	Fin Para
	
	prom= (suma+num)/(cantidadDeIteraciones+1); 
	Escribir "La suma de todos los numeros ingresados es: ", suma+num; 
	Escribir "El promedio de la suma de todos los numeros ingresados es: ", prom; 
	Escribir "El valor maximo ingresado es: ", max; 
	Escribir "El valor minimo ingresado es: ", min; 
FinFuncion

Funcion Ejercicio4
	definir n, div, cant1, cant2, i  Como Entero; 
	cant2= 0; 
	Escribir "INgrese la cantidad de numeros a Analizar";
	leer cant1; 
	
	Repetir
		Escribir "Ingrese un numero";
		leer n; 
		
		si n<=0 Entonces
			Escribir "Ingresó un numero negativo"; 
		SiNo
			si n>0 Entonces
				cant2=cant2+1; 
				div=0; 
				
				Para i<-1 Hasta n Hacer
					si (n%i)=0 Entonces
						div= div+1; 
					FinSi
				Fin Para
				
				Si div>2 Entonces
					Escribir n, " no es un numero primo";
				SiNo
					si div<=2 Entonces
						Escribir n, " es un numero primo"; 
					FinSi
				FinSi
			FinSi
		FinSi
	Mientras Que cant2<cant1; 
FinFuncion

Funcion Ejercicio5
	definir num, invertido, original, digito Como Entero
		Escribir "Ingrese un numero entero";
		leer num; 
		original=num; 
		invertido=0; 
		
		Mientras num>0 Hacer
			digito= num%10;
			invertido= invertido*10+digito; 
			num= trunc(num/10)
		Fin Mientras
		
		si num <0 Entonces
			Escribir "Ingresó un numero negativo"; 
		SiNo
			si original=invertido Entonces
				Escribir "El numero es capicula";
			SiNo
				Escribir "No es capicua. El numero es: ", invertido; 
				
			FinSi
		FinSi
		
FinFuncion

Funcion Ejercicio6
	Definir N, i, j, M, contador,contadorPorFamilia, edad, sumaPorFamilia, sumaTotal Como Entero
	Definir promPorFamilia, promTotal como real; 
	Escribir "Ingrese la cantidad de familias que hay"; 
	Leer N; 
	contador=0; 
	sumaTotal= 0; 
	promTotal=0; 
	
	si N<0 Entonces
		Escribir "Ingresó un numero erroneo"; 
	SiNo
		Para i<-1 Hasta N Con Paso 1 Hacer
			Escribir "Ingrese la cantidad de hijos que tiene la familia ", N;
			Leer M
			contadorPorFamilia=0; 
			sumaPorFamilia=0; 
			si M<0 Entonces
				Escribir "Ingresó un numero erroneo";
			SiNo
				Para j<-1 Hasta M Con Paso 1 Hacer
					Escribir "Ingrese la edad del hijo ", M; 
					Leer edad; 
					contadorPorFamilia=contadorPorFamilia+1
					sumaPorFamilia= sumaPorFamilia+edad; 
				Fin Para
				promPorFamilia=sumaPorFamilia/contadorPorFamilia
				Escribir "El promedio de la familia ", M, " es de: ", promPorFamilia;
				sumaTotal= sumaTotal+sumaPorFamilia;
			FinSi
			contador= contador+1; 
		Fin Para
		promTotal= sumaTotal/contador; 
		Escribir "El promedio total es de: ", promTotal; 
	FinSi
	
FinFuncion

funcion Ejercicio7
	Definir i, num, contador, contadorPar, sumaDiv7, contadorMultiplo3, sumaMult3 Como Entero
	contador=0;
	contadorPar=0; 
	sumaDiv7=0; 
	contadorMultiplo3=0; 
	sumaMult3=0; 
	
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Repetir
			Escribir "Ingrese un numero entero positivo que quedará en la posicion ", i; 
			Leer num
		Mientras Que num<0
				
		si num%2=0 Entonces
			contadorPar=contadorPar+1;  
		SiNo
			contador= contador+1;
		FinSi
		
		si num%7=0 Entonces
			sumaDiv7=sumaDiv7+num; 
		FinSi
		
		si num%3=0 Entonces
			contadorMultiplo3=contadorMultiplo3+1;
			sumaMult3=sumaMult3+num; 
		FinSi
		
		
	Fin Para
	
	si contador=0 Entonces
		Escribir "No ingresó ningun numero impar"
	SiNo
		si contador>0 Entonces
			Escribir "La cantidad de numeros impares que se ingresó es de: ", contador; 
		FinSi
	FinSi
	
	si sumaDiv7>0 Entonces
		Escribir "La suma de todos multiplos de 7 es de: ", sumaDiv7; 
	SiNo
		Escribir "No ingresó un multiplo de 7"; 
	FinSi
	
	si contadorMultiplo3>0 Entonces
		Escribir "El promedio de la suma de los multiplo de 3 es de: ", sumaMult3/contadorMultiplo3
	SiNo
		Escribir "No se ingresó ningun numero multiplo de 3"; 
	FinSi
	
FinFuncion

Funcion Ejercicio8
	Definir option Como entero;
	Definir n1, n2 como real;
	definir rta Como Caracter;
	
	n1=0;
	n2=0; 
	Repetir
		Escribir "-------------------------------"; 
		Escribir "            MENÚ"; 
		Escribir "-------------------------------"; 
		Escribir "      1-Ingresar Operandos     "; 
		Escribir "      2-Sumar     ";
		Escribir "      3-Restar     ";
		Escribir "      4-Multiplicar     ";
		Escribir "      5-Dividir     ";
		Escribir "      6-Salir     ";
		Escribir "-------------------------------"; 
		leer option; 
		rta="n"
		
		Segun option Hacer
			1:
				Repetir
					
					Escribir "Ingrese los numeros que desee sumar. Estos no deben ser 0"
					leer n1, n2; 
					si n1=0 o n2=0 Entonces
						Escribir "ingresó un valor 0. Debe ingresar valores diferentes a 0";
					FinSi
				Mientras Que n2=0 o n1=0
				
			2:
				si n1=0 y n2=0 Entonces
					Escribir "Debe pasar por la opcion 1"
				SiNo
					escribir "la suma de ", n1, " y ", n2, " es: ", n1+n2;
				FinSi
			3:
				si n1=0 y n2=0 Entonces
					Escribir "Debe pasar por la opcion 1";
				SiNo
					escribir "la resta de ", n1, " y ", n2, " es: ", n1-n2;
				FinSi
				
			4: 
				si n1=0 y n2=0 Entonces
					Escribir "Debe pasar por la opcion 1";
				SiNo
					escribir "la multiplicacion de ", n1, " y ", n2, " es: ", n1*n2;
				FinSi
				
			5: 
				si n1=0 y n2=0 Entonces
					Escribir "Debe pasar por la opcion 1";
				SiNo
					escribir "la division de ", n1, " y ", n2, " es: ", n1/n2;
				FinSi
			6:
				Escribir "¿Esta seguro que quiere salir de la aplicacion?(s/n)";
				leer rta;
				rta= Minusculas(rta)
			De Otro Modo:
				Escribir "Ingresó una opcion erronea";
		Fin Segun
	Mientras Que rta<>"s"
FinFuncion

Funcion Ejercicio9
	Definir cantPizzas,i, option,option2, total, pizzaVeg, PizzaNoVeg, PizzaBas, IngredVeg, IngredNoVeg  Como Entero; 
	definir salir Como Entero; 
 	total=0; 
	pizzaVeg=15000; 
	PizzaNoVeg=20000;
	PizzaBas=10000;
	IngredVeg=5000;
	IngredNoVeg=7000;
	salir= 0
	
	Repetir
		Escribir "------------------"; 
		Escribir "Pizerria Bella Napoli"; 
		escribir "------------------"; 
		Escribir "Nuestro Menú"
		escribir "1.Pizza basica $10000"; 	
		escribir "2.Pizza vegetariana $15000. Ingrediente extra $5000 "; 	
		escribir "3.Pizza no vegetariana $20000. Ingrediente extra $7000"; 	
		escribir "4.Finalizar";
		escribir "¿Cuantas pizzas desea llevar?"; 
		Leer cantPizzas; 
		
		
		Para i<-1 Hasta cantPizzas Con Paso 1 Hacer
			Escribir "Segun nuestro menú, que tipo de pizzas quiere?"
			leer option;
				Segun option Hacer
					1:
						Escribir "Uds lleva una pizza basica que contiene Muzzarella y salsa"
						total= PizzaBas;
					2:
						Escribir "Uds quiere una pizza vegetariana. Esta puede llevar Pimiento o tofu";
						Escribir "1. Pimiento"
						Escribir "2.Tofu"
						leer option2; 
						Segun option2 Hacer
							1: Escribir "Su pizza tiene, ademas de muzzarella y salsa, tiene pimiento";
								total= total+pizzaVeg+IngredVeg;
							2:Escribir "Su pizza tiene, ademas de muzzarella y salsa, tiene tofu";
								total= total+pizzaVeg+IngredVeg;
						FinSegun
					3:
						Escribir "Uds quiere una pizza No vegetariana. Esta puede llevar Jamon, salmon o peperoni";
						Escribir "1. Jamon"
						Escribir "2.Salmon"
						Escribir "3. Peperoni"
						leer option2; 
						Segun option2 Hacer
							1: Escribir "Su pizza tiene, ademas de muzzarella y salsa, tiene jamon";
								total= total+PizzaNoVeg+IngredNoVeg;
							2:Escribir "Su pizza tiene, ademas de muzzarella y salsa, tiene Samon";
								total= total+PizzaNoVeg+IngredNoVeg;
							3:Escribir "Su pizza tiene, ademas de muzzarella y salsa, tiene Peperoni";
								total= total+PizzaNoVeg+IngredNoVeg;
							De Otro Modo:
								Escribir "Opcion incorrecta"
						FinSegun
					4:salir=1; 
					De Otro Modo:
						Escribir "Opcion Incorrecta"
				Fin Segun
		Fin Para
	Mientras Que salir=0
	Escribir "El total de su compra es de: ", total; 
FinFuncion

funcion Ejercicio10
	Definir n, i, j Como Entero
    Escribir "Ingrese el número de filas del triángulo invertido: "
    Leer n
	
    Para i <- n Hasta 1 Con Paso -1 Hacer
        Para j <- 1 Hasta i Hacer
            Escribir Sin Saltar "*"
        FinPara
        Escribir "" // Esto es para pasar a la siguiente línea
    FinPara

FinFuncion
