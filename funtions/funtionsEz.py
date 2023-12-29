def suma(*args):
    args_list = list(args)
    for arg in args:
        suma = sum(args_list)
    return suma
def multiplicacion(*args):
    resultado = 1
    for arg in args:
        resultado *= arg
    return resultado
print(suma(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
print(multiplicacion(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))


#key and value function
def dictionary(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

dictionary = {}

def funtionTest(dictionary, newKeyValues):
    for key, value in newKeyValues.items():
        if isinstance(key, int):
            dictionary[key] = value
    return dictionary

dictionary = funtionTest(dictionary, {1: "hola", 2: "mundo"})
print(dictionary)

dictionary = funtionTest(dictionary, {23: "Kendall", 2: "kendasfafga"})
print(dictionary)