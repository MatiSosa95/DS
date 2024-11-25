Algoritmo TPractico
	//Elija que ejercicio quiere ver aqui abajo. 
	Ejercicio2;
	
FinAlgoritmo

Funcion Ejercicio1
	Escribir "El verdadero desafío es imaginarte el algoritmo y no programarlo";
FinFuncion

Funcion Ejercicio2
	Definir nickname Como Caracter;//Es un cadena de texto
	Definir cumple Como Caracter; // Es una cadena
	Definir edad Como Entero;//Es un numero entero
	Definir factura Como Real; //Es un numero real
	Definir compra Como Caracter; // Es una cadena de texto
	
	nickname= "Arigaruton"; 
	cumple= "8 de marzo"; 
	edad=29; 
	factura= 8100.00; 
	compra = "Comics de Star wars";
	
	Escribir "Mi nickname es ", nickname, " y es una variable cadena. Mi edad es ", edad, " y es una variable Entera y cumplo el ", cumple, " que es una varibale cadena, Hace poco compre ", compra, ", que es una variable cadena y salió ", factura, " la cual es una variable real "; 
FinFuncion

Funcion Ejercicio3
	Definir materiaPreferida Como Caracter; 
	Definir pasatiempo Como Caracter;
	Definir deporte Como Caracter;
	Definir familia Como Entero;
	Definir nroDeMascota Como Entero;
	
	Escribir "Escriba su materia preferida";
	Leer materiaPreferida; 
	
	Escribir "Escribir su pasatiempo "; 
	Leer  pasatiempo; 
	
	Escribir "¿Que deporte hace?";
	Leer deporte; 
	
	Escribir "¿Cuantas personas hay en su familia?"; 
	Leer familia; 
	
	Escribir "¿Cuantas mascotas tiene?"; 
	Leer nroDeMascota; 
	
	Escribir "Mi materia preferida en el colegio es ", materiaPreferida,". Mi pasatiempo preferido es ", pasatiempo,". Practico  " , deporte ," como deporte", ". En mi familia somos ", familia," y ", nroDeMascota , " mascotas";
FinFuncion

Funcion Ejercicio4
	Definir edad, edadFuturo,edadACalcular, anoDeNac, anoActual Como Entero; 
	anoActual=2024;
	edad=0; 
	Escribir "Ingrese el año en que nació"; 
	Leer anoDeNac;
	Escribir "Ingrese el año para que calcule su edad";
	Leer edadACalcular
	
	edad= anoActual-anoDeNac;
	edadFuturo= edadACalcular-anoDeNac; 
	
	
	Escribir "Mi edad actualmente es de ",edad," años, por lo cual en el ",edadACalcular, " tendré ", edadFuturo, " años" ; 
FinFuncion

Funcion Ejercicio5
	Definir pagoMesAnteriorGas, pagoActualGas Como Real;
	Definir porcetaje Como Entero; 
	Escribir "Ingrese el monto de su anterior factura de gas"; 
	Leer pagoMesAnteriorGas; 
Escribir "Ingrese el porcentaje del aumento";
	Leer porcetaje;
	
	pagoActualGas= pagoMesAnteriorGas+(pagoMesAnteriorGas*(porcetaje/100));
	
	Escribir "El mes de abril pagué ",pagoMesAnteriorGas, " pesos de gas, y este mes deberé pagar ", pagoActualGas, " pesos como mínimo";
	
FinFuncion

	