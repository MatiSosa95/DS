Algoritmo SentenciasCondicionales
	TesteandoElNumeroCentral; 
	
FinAlgoritmo

funcion TesteandoElNumeroMayor
	//Entrada: 3 numeros enteros
	//Salida:Mensaje de cual es el mayor
	Definir a,b,c Como Entero;
	
	Escribir "Ingrese los valores de a , b y c";
	Leer a,b,c; 
	
	si a=b y b=c Entonces
		Escribir "Todos los valores son iguales";
	sino 
		si a<c y b<c Entonces
			Escribir "C es el mayor. Su valor es ", c;
		SiNo
			si b<a y c<a Entonces
				Escribir "A es el mayor. Su valor es ", a;
			SiNo
				Escribir "B es el mayor. Su valor es ", b;
			FinSi
		FinSi
	FinSi
FinFuncion

funcion TesteandoElNumeroCentral
	//Entrada: 3 numeros enteros
	//Salida: Mensaje de cual es el valor central
	Definir a,b,c Como Entero;
	Leer a,b,c; 
	si a=b y b=c Entonces
		Escribir "Todos los valores son iguales y no hay numero central";
	SiNo
		si a=b o a=c o b=c Entonces
			Escribir "No existe valor central";
		SiNo
			si (a>b y a<c) o (a>c y a<b) Entonces
				Escribir "A es el valor central. Su valor es ", a;
			SiNo
				si (b>a y b<c) o (b>c y b<a) Entonces
					Escribir "B es el valor central. Su valor es ", b;
				SiNo
					Escribir "C es el valor central. Su valor es ", c;
				FinSi
			FinSi
		FinSi
	FinSi
FinFuncion

Funcion  VerificarTipoDeTriangulo
	//Entrada: 3 longitudes
	//Salida: Mensaje si forman un triangulo o no, y cual de ellos. 
	Definir a,b,c Como real;
	Escribir "Ingrese 3 longitudes";
	Leer a,b,c; 
	
	si (a+b<=c) o (c+b<=a) o (a+c<=b) Entonces
		Escribir "No es un triangulo";
	SiNo
		si a=b y a=c Entonces
			Escribir "Se forma un triangulo equilatero";
		SiNo
			si a=b y a<>c Entonces
				Escribir "Se forma un triangulo isoceles"
			SiNo
				si a<>b y a<>c y c<>b Entonces
					Escribir "Se forma un triangulo escaleno"; 
				FinSi
			FinSi
		FinSi
	FinSi
FinFuncion

funcion PizzaVegetariana
	//Entrada: Si quiere pizza vegetariana o no  y cual es el agregado
	//Salida: Si la pieza es vegetariana o no y el agregado que le puso el cliente
	definir tipoPizza, ingredienteBase, ingredientes, in como caracter; 
	ingredienteBase= "mozzarella, salsa de tomate"; 
	Escribir "Quiere una pizza vegana o no? (si/no)";
	leer tipoPizza;
	
	si tipoPizza="si" o tipoPizza="SI" Entonces
		Escribir "Los ingredientes disponibles para vegetarianos son: tofu y pimiento";
		leer ingredientes;
		in= Minusculas(ingredientes)
		si (in = "tofu") o (in = "pimiento") Entonces
			
			Escribir "Su pizza es vegetariana y contiene: ", ingredienteBase, " y ", ingredientes;
		SiNo
			Escribir "Ingresó un ingrediente erroneo"; 
		FinSi
	SiNo
		Escribir "Ingredientes disponible para no vegetarioanos son: Jamon, Salmon y Peperoni"; 
		Leer ingredientes;
		in= Minusculas(ingrediente);
		si (in = "jamon") o (in = "salmon") o (in = "peperoni")  Entonces
			
			Escribir "Su pizza es no vegetariana y contiene: ", ingredienteBase, " y ", ingredientes;
		SiNo
			Escribir "Ingresó un ingrediente erroneo"; 
		FinSi
	FinSi
	
FinFuncion

funcion CalculadoraBasica
	//Entrada: numeros y la operacion que desea Hacer
	//Salida: El resultado de la operacion
	Definir option Como Caracter;
	Definir n1, n2 como real;
	Escribir "Ingrese los numeros que desee sumar"
	leer n1, n2; 
	Escribir "Elija la operacion que desea hacer. S para suma, R para resta, M para multiplicacion y D para division";
	leer option; 
	
	Segun option Hacer
		"S","s": 
			escribir "la suma de ", n1, " y ", n2, " es: ", n1+n2;
		"R", "r":
			escribir "la resta de ", n1, " y ", n2, " es: ", n1-n2;
		"M", "m":
			escribir "la multiplicacion de ", n1, " y ", n2, " es: ", n1*n2;
		"D", "d":
			si n2<>0 Entonces
				escribir "la division de ", n1, " y ", n2, " es: ", n1/n2;
			SiNo
				Escribir "El resultado de dividir un numero por 0 es una indeterminacion"; 
			FinSi
		De otro modo: 
			Escribir "La opcion ingresada no es valida";
	FinSegun
FinFuncion

funcion DocenaDeEmpanadas
	//Entrada: Cantidad de producto a comprar en docenas
	//Salida: Monto a pagar y el numero de unidades de obsequio. 
	Definir cantProd, cantDeDocenas, prodExtra Como Entero; 
	Definir precioXUnidad, precio, descuento Como Real;
	Escribir "Ingrese la cantidad de docenas que desea comprar";
	Leer cantDeDocenas; 
	
	cantProd= cantDeDocenas*12;
	precioXUnidad= 500.00;
	
	si cantDeDocenas>3 Entonces
		prodExtra= cantDeDocenas-3;
		descuento= (cantProd*precioXUnidad)*0.15;
		Escribir "El numero de unidades de regalos es de " , prodExtra, " y el total de productos que se lleva es de ", prodExtra+cantProd ; 
	SiNo
		si cantDeDocenas<=3 y cantDeDocenas>=1
			descuento= (cantProd*precioXUnidad)*0.10;
		SiNo
			Escribir "Ingresó un numero erroneo";
		FinSi
	FinSi
	
	precio= (cantProd*precioXUnidad)-descuento;
	escribir "El monto total de la compra es de ", cantProd*precioXUnidad;
	escribir "El monto que debe pagar es de ", precio;
	Escribir "El descuento hecho es de ", descuento;
FinFuncion
	