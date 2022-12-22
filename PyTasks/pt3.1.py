#Create a user defined function to find compound interest.
def comint(p,r,n,t):
    A=p*((1+(r/n))**(n*t))
    print("Amount is:",A)
    print("Compound Interest is:",(A-p))
print("Create a user defined function to find compound interest.\n")
p=float(input("Enter Principle Amount: "))
r=float(input("Enter Annual Nominal Rate: "))
n=float(input("Enter number of times the interest is compounded per year: "))
t=float(input("Enter number of year: "))
comint(p,r,n,t)