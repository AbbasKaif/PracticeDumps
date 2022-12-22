#Create a currency convertor by using concept of function and ladder if – else.
print("Create a currency convertor by using concept of function and ladder if – else.\n")
print("Enter 1 for Dollar to Rupee\nEnter 2 for Rupee to Dollar")
ch=int(input("Enter your choice: "))
if ch==1:
    a=float(input("Enter Amount in Dollar: "))
    print(a,"USD =",round((a*69.0225),2),"INR")
elif ch==2:
    a=float(input("Enter Amount in Rupees: "))
    print(a,"INR =",round((a*0.0144875),2),"USD")
else:
    print("Invalid Choice")