#Develop a program in python to create a list of 10 integer nos. Now find sum and average of these numbers.
print("Program in python to create a list of 10 integer nos. Now find sum and average of these numbers.\n")
sum=0
list=[]
for i in range(1,11):
    n=int(input("Enter Integer: "))
    list.insert(i,n)
for i in range(0,len(list)):
    sum=sum+list[i]
print("Sum is: ",sum)
print("Average is:",(sum/len(list)))