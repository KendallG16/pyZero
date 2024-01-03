def factorial(numero):
    if numero == 1:
        return 1
    elif numero == 0:
        return 0
    else:
        return numero * factorial(numero - 1)
numero = factorial(9)
print(numero)