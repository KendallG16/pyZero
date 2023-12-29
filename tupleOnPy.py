#the tuple are immutable, so you can't change the values
names =  ("John", "Mary", "Peter", "Jane")
print(names[0:4])

for i in names: 
    if i == "Jane":
        print("Jane is in the tuple")
    else:
        print("Jane is not in the tuple")

#this is not recomended, but is you need to change the values of a tuple, you can do this:
names = list(names)
list_numbers = []
numbers = (1,2,3,4,5,6,7,8,9,10)
for i in numbers:
    if i < 5:
        list_numbers.append(i)
        print(list_numbers)

nombre = input("ingrese el nombre a consultar: ")    

if nombre in names:
    print("Jane is in the tuple")

#discard no arroja error en caso de no encontrar el valor
#remove arroja error en caso de no encontrar el valor
#del lo borra completamente