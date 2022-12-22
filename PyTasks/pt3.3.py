#Write a program in python to find factorial of given number using ‘Recursion’.
print("Python to find factorial of given number using ‘Recursion’.\n")
def fact(n):
    if(n==1):
        return n
    else:
        return(n*fact(n-1))
num=int(input("Enter a number: "))
print("Factorial is:",fact(num))