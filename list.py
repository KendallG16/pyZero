names = ["Kendall", "Kylie", "Kris", "Caitlyn", "Kim", "Khloe", "Kourtney", "Rob", "Kanye", "North", "Saint", "Chicago", "Psalm"]

def print_list():
    for i in names:
        print (i)
print_list()

def print_list2():
    print (names[0:13], end=" ")
    print (names[0:13:2], end=" ")
    print (names[:13], end=" ")
    print (len(names))
print_list2()   
#print names whitout [] and ''
print(f"This is a name list: {" ".join(names)}")