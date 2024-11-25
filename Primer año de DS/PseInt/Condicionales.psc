Algoritmo Condicionales
	EjemploDeestructuraAnidadas; 
FinAlgoritmo

Funcion CondicionalSimple
	//Entrada: año De nacimiento, año actual y edad minima para votar
	//Calcular la edad y verificar si tiene edad para votar
	//Salida: Mensaje por pantalla donde indica que puede votar
	
	Definir anoActual, anoDeNac, edadMin, edad Como Entero; 
	edadMin=16;
	Escribir "Ingrese el año en que nacio";
	Leer anoDeNac;
	
	Escribir "Ingrese el año actual ";
	Leer anoActual;
	
	edad= anoActual-anoDeNac;
	
	si edad>=edadMin Entonces
		Escribir "Su edad es de ",edad,". Ud puede votar";
		
	FinSi
FinFuncion

Funcion CondicionalDoble
	
	//Entrada: Nota1, Nota2, Nota3
	//Salida: mensaje si aprobó o no aprobó
	
	Definir nota1, nota2, nota3 Como Entero;
	Definir prom como real;
	
	Escribir "Ingrese el valor de la nota 1";
	Leer  nota1; 
	
	Escribir "Ingrese el valor de la nota 2";
	Leer  nota2; 
	
	Escribir "Ingrese el valor de la nota 3";
	Leer  nota3; 
	
	prom= (nota1+nota2+nota3)/3; 
	
	si prom>=7 Entonces
		Escribir "Su nota es: ", prom, ". Uds aprobó"; 
	SiNo
		Escribir "Su nota es: ", prom, ". Uds no aprobó"; 
	FinSi
FinFuncion

Funcion esPar
	//Entrada: Un numero entero
	//Salida: Mensaje si es par o impar. 
	Definir num Como Entero; 
	
	Escribir "Ingrese un numero entero";
	Leer num;
	
	si num%2=0 Entonces
		Escribir "Es par"; 
	SiNo
		Escribir "Es impar";
	FinSi
FinFuncion

Funcion CondicionalMultiple
	//Entreda: nombre de serie y la calificacion.
	//Salida: Mensaje si es una serie recomendada o no. 
	
	definir estrellas Como Entero;
	definir serie Como Caracter; 
	
	Escribir "Ingrese el nombre de la serie que quiere clasificar";
	Leer serie; 
	
	
	Escribir "Ingrese la cantidad de estrellas le asignariaa la serie ", serie,". Recuerde que puede poner 1 a 5 estrellas"
	Leer estrellas;
	
	si estrellas>=1 y estrellas<=5 Entonces
		Segun estrellas Hacer
			1: 	escribir serie, ". No es un serie muy recomendable";
			2:	escribir serie, ". No es un serie recomendable";
			3:	escribir serie, ". Es un serie medianamente recomendable";
			4:	escribir serie, ". Es una serie recomendable";
			5:	escribir serie, ". Es una serie muy recomendable";
			De Otro Modo:
				Escribir "Ingresó un valor erroneo";
		FinSegun
	SiNo
		Escribir "Numero erroneo";
	FinSi
	
	
	
FinFuncion

Funcion romanos
	//Entrada: Un numero entero
	//Salida: mensaje con el numero convertido
	Definir num Como Entero; 
	Escribir "Ingrese un numero entero entre el 1 al 10"; 
	leer num; 
	si num>=1 y num<=10 Entonces
		Segun num hacer
			1:	escribir "El numero : ", num, " en numeros romanos es: I"; 
			2:	escribir "El numero : ", num, " en numeros romanos es: II"; 
			3:	escribir "El numero : ", num, " en numeros romanos es: III"; 
			4:	escribir "El numero : ", num, " en numeros romanos es: IV"; 
			5:	escribir "El numero : ", num, " en numeros romanos es: V"; 
			6:	escribir "El numero : ", num, " en numeros romanos es: VI"; 
			7:	escribir "El numero : ", num, " en numeros romanos es: VII"; 
			8:	escribir "El numero : ", num, " en numeros romanos es: VIII"; 
			9:	escribir "El numero : ", num, " en numeros romanos es: IX"; 
			10:	escribir "El numero : ", num, " en numeros romanos es: X"; 
			De Otro Modo:
				Escribir "El numero no se puede convertir";
		FinSegun
	SiNo
		Escribir "El numero ingresado fuera de rango"; 
		
	FinSi
FinFuncion

Funcion OperadoresLogicos
	Definir nombreMateria Como Caracter;
	Definir nota Como Entero;
	Definir asistencia Como Real;
	
	Escribir "Ingrese el nombre de la materia"
	Leer nombreMateria; 
	Escribir "Ingrese la nota de la materia";
	Leer nota;
	Escribir "Ingrese el porcentaje de la asistencia del alumno"; 
	Leer asistencia; 
	
	asistencia= asistencia/100;
	
	si nota>=6 y asistencia>=0.8 Entonces
		Escribir "aprobó ", nombreMateria;
	SiNo
		Escribir "Ud no aprobó ", nombreMateria; 
		
	FinSi
FinFuncion

Funcion ejemploDeOperadoresLogicos
	Definir precioEntrada Como Entero
	Definir estud, egres , doc Como Caracter
	Definir estudiante, egresado, docente Como Logico
	Definir descuento Como Real;
	
	precioEntrada=9000; 
	descuento= .5;
	
	Escribir "Uds es docente?"
	Leer doc;
	
	Escribir "Uds es egresado?"
	Leer egres;
	Escribir "Uds es estudiante?"
	Leer estud;
	
	si estud= "si" Entonces
		estudiante=Verdadero	
	SiNo
		estudiante= Falso
	FinSi
	
	si egres ="si"  Entonces
		egresado=Verdadero	
	SiNo
		egresado= Falso
	FinSi
	
	si doc= "si" Entonces
		docente=Verdadero	
	SiNo
		docente= Falso
	FinSi
	
	si estudiante=Verdadero O egresado=Verdadero O docente=Verdadero Entonces
		Escribir "Uds tiene el 50% de descuento, por lo tanto pagará ", precioEntrada*descuento;
	SiNo
		Escribir "Uds debe pagar ", precioEntrada;
		
	FinSi
FinFuncion

Funcion estructuraAnidadas
	Definir A, B Como entero
	
	Escribir "Ingrese dos numeros";
	Leer A, B; 
	
	si A>B Entonces
		Escribir A, " es mayor que ", B; 
	SiNo
		si A<B Entonces
			Escribir B, " es mayor que ", A;
		SiNo
			Escribir A," es igual a ",B;
		FinSi
		
	FinSi
FinFuncion

Funcion EjemploDeestructuraAnidadas
	Definir nota como real; 
	
	Escribir "Ingrese la nota del alumno"; 
	Leer nota; 
	
	si nota>=7 y nota<=10 Entonces
		Escribir "El alumno tiene la promocion Directa";
	SiNo
		si nota>=1 y nota <=3 Entonces
			Escribir "El alumno esta aplazado y debe recursar"
		SiNo
			Escribir "El alumno está regular";
		FinSi
	FinSi
	
	
	
	
	
	
FinFuncion
	