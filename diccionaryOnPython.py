computersParts = {
    "TM": "tarjeta madre",
    "CPU": "procesador",
    "RAM": "memoria de acceso aleatorio",
    "SSD o HDD ": "solid state drive o hard disk drive"
}

print(computersParts["TM"])
print(computersParts.get("CPU"))
print(computersParts)
#key and value
for key, value in computersParts.items():
    print(key, value)
#just key
for key in computersParts.keys():
    print(key)
#just value
for value in computersParts.values():
    print(value)
#add new key and value
computersParts["hola"] = "mundo"
print(computersParts)

computersParts.update({"hola": "mundoooo"})
print(computersParts)

computersParts.pop("hola")
print(computersParts)   