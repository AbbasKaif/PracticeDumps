print("Write a program in python to create a module tempconv.py, with two functions ctof() and ftoc(). ctof() converts temperature from centigrade to forenhite and ftoc() converts temperature from farenhite to centigrade. Now test the module tempconv.")
import tempconv
print("Enter 1 for C to F \nEnter 2 for F to C")
ch=int(input("Enter your choice: "))
if ch==1:
	a=float(input("Enter temperature in C "))
	print(tempconv.ctof(a),"F")
elif ch==2:
	a=float(input("Enter temperature in F "))
	print(tempconv.ftoc(a),"C")
else:
	print("Wrong Choice!")