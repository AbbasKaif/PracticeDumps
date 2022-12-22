#Sum of digits
print("Program to find sum of digits of given number.\n")
num=int(input("Enter a number: "))
sum=0
while(num>0):
    p,q=divmod(num,10)
    sum=sum+q
    num=p
print("Sum of digits is",sum)


num=int(input("Enter a number: "))
sum=0
while(num>0):
    sum=sum+(num%10)
    num=int(num/10)                 #num=num//10
print("Sum of digits is",sum)