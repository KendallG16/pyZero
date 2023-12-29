def ingresoCasas() -> int:
    try:
        casa = input("ingrese el numero de la casa: ")
    except ValueError:
        print("El valor ingresado no es válido")
        return None 
    return int(casa)

def nombrePropietario() -> str:
    nombrePropietario = input("ingrese el nombre del propietario: ")
    return str(nombrePropietario)

def casas(homesList) -> dict:
    ingresos = int(input("¿Cuántas casas desea ingresar?: "))
    for _ in range(ingresos):
        key = ingresoCasas()
        if key is int:
            value = nombrePropietario()
            homesList[key] = value
    return homesList



homesList = {}

while True:
    cases = int(input(" Salir = 1 \n Ingresar casas = 2: "))
    match cases:
        case 1:
            print(homesList)
        case 2:
            homesList = casas(homesList)


def lista(*args):
    for arg in args:
        print(arg)
    print(args)