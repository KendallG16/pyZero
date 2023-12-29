homesList = {}

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

def casas (homesList) -> dict:

    numCasas = 0
    try:

        ingresos = int(input("¿Cuántas casas desea ingresar?: "))
    
    except ValueError:
    
        print("El valor ingresado no es válido")
    
        return None, None
    
    for _ in range(ingresos):
        numCasas += 1
        
        casa = ingresoCasas()
        if casa is None: break
       
        
        propietario = nombrePropietario() 
        homesList[casa] = propietario  

    return homesList, numCasas

def main(homesList) -> dict:
    homesList, _ = casas(homesList)
    print(homesList)


while True:
    cases = int(input(" Salir = 1 \n Ingresar casas = 2: "))
    match cases:
        case 1:
            print(homesList)
        case 2:
            main(homesList)


def lista(*args):
    for arg in args:
        print(arg)
    print(args)