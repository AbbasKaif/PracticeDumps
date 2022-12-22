#Develop a program in python to copy elements of one list to another list.
print("program in python to copy elements of one list to another list.\n")
lista,listb=[],[]
for i in range(1,11):
    n=int(input("Enter Integer: "))
    lista.insert(i,n)
for i in range(0,10):
    listb.insert(i,lista[i])
print(lista)
print(listb)