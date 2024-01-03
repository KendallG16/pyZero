def decreciente (numero):
    if numero == 0:
        return 0
    else:
        print(numero)
        return decreciente(numero - 1)
    
def calculator(saldo:float, impuesto:float) -> float: 
    if saldo <=  0:
        print("El saldo tiene que ser mayor que 0, intentelo de nuevo")
        return calculator()
    else:
        pass
    print(f'El saldo total es de: {saldo + (saldo * (impuesto/100))}')

def celToFar(celsius):
    fahrenheit = ((celsius * (9/5))+32)
    return fahrenheit
def fahrToCelsius(fahrenheit):
    celcius = ((fahrenheit -32) / (9/5))
    return celcius

celToFar = celToFar(90)
print(celToFar , "\n")

fahrToCelsius = fahrToCelsius(90)
print(fahrToCelsius)