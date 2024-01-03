class Persona():
    def __init__(self, nombre : str, edad : int, estatura : float) -> object:
        self.nombre = nombre 
        self.edad = edad
        self.estatura = estatura

def crearPersona(personas:list):
    cantidad = int(input("Ingrese cuantas personas quiere crear: "))
    for _ in range(cantidad):   
        nombre =  input("Ingrese el nombre de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        estatura = float(input("ingrese la altura de la persona: "))
        persona_nueva = Persona(nombre, edad, estatura)
        personas.append(persona_nueva)
    return personas

def borrarPersona(personas):
    personaEliminar = input("Ingrese el nombre de la persona a eliminar: ")
    for i in range(len(personas)):
        if personas[i].nombre == personaEliminar:
            del personas[i]
            break
    return personas

def mostrarPersonas(personas):
    for i, persona in enumerate(personas, 1):
        print(f"{i}. Nombre: {persona.nombre}, Edad: {persona.edad}, Estatura: {persona.estatura}")

def modificarDatos(personas):
    personaModificar = input("Ingrese el nombre de la persona que quiere modificar: ")
    for i in range(len(personas)):
        if personas[i].nombre == personaModificar:
            dato = int(input(f'Nombre: 1 \n Edad: 2 \n Estatura: 3 \n Ingrese la opcion a modificar: \n'))
            match(dato):
                case 1:
                    personas[i].nombre = input("Ingrese el nuevo nombre: ")
                case 2:
                    personas[i].edad = int(input("Ingrese la nueva edad: "))
                case 3:
                    personas[i].estatura = float(input("Ingrese la nueva estatura: "))
personas = []


crearPersona(personas)

mostrarPersonas(personas)

borrarPersona(personas)

mostrarPersonas(personas)

modificarDatos(personas)