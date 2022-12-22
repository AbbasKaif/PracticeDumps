#Program to convert temperature from C to F or F to C as per user's choice.

print("Enter 1 for C to F \nEnter 2 for F to C")
ch=int(input())
if ch==1:
	a=float(input("Enter temperature in C "))
	print((a*(9/5))+32,"F")
elif ch==2:
	a=float(input("Enter temperature in F "))
	print((a-32)*(5/9),"C")
else:
	print("Wrong Choice!")