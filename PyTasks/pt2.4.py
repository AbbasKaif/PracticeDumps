#Develop a program in python to create a list of 10 integer nos. by taking input from user. Now find maximum and minimum numbers.
print("Program in python to create a list of 10 integer nos. by taking input from user. Now find maximum and minimum numbers.\n")
list=[]
for i in range(1,11):
    n=int(input("Enter Integer: "))
    list.insert(i,n)
print(max(list))
print(min(list))