#Registro de alumnos
lista_alumnos =dict()
i = 1
class Alumnos:
    def __init__(self,id,  nombre, apellido, edad, curso, nota):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso
        self.nota = nota

    def calcular_promedio(self):
        return sum(self.nota) / len(self.nota)

    def mostrar_info(self):
        print("ID: ", self.id)
        print("Nombre: "+ self.nombre)
        print("Apellido: " + self.apellido)
        print("Edad: " + self.edad)
        print("Curso: " + self.curso)
        print("Nota: ", self.calcular_promedio())

def guardar_alumno(alumno):
    global i
    if alumno.id not in lista_alumnos:
        lista_alumnos[i] = alumno
        i+=1

def main():
    global i
    while True:
        print("Menú de opciones\n0. Salir\n1. Cargar un alumno\n2. Mostrar alumno por ID\n3. Mostrar alumnos")
        opcion = int(input())
        if opcion == 1:
            lista_notas =[]
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            apellido_alumno = input("Ingrese el apellido del alumno: ")
            edad_alumno = input("Ingrese el edad del alumno: ")
            curso_alumno = input("Ingrese el curso del alumno: ")
            for j in range(3):
                notas = int(input(f"Ingrese la {j+1}° nota del alumno: "))
                lista_notas.append(notas)
            alumnos = Alumnos(i, nombre_alumno, apellido_alumno, edad_alumno, curso_alumno, lista_notas)
            guardar_alumno(alumnos)
        if opcion == 2:
            id = int(input("Ingrese un ID del alumno: "))
            existe = False
            for i, j in lista_alumnos.items():
                if i == id:
                    j.mostrar_info()
                    existe = True

            if not existe:
                print("El alumno no existe")

        if opcion == 3:
            for alumno in lista_alumnos.values():
                print(alumno.mostrar_info())

        if opcion == 0:
            print("Saliendo...")
            break


main()





