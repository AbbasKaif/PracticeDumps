#Convert days to year

a=int(input("Enter Number of Days "))
print(int((a/365)),"year(s)",int((int((a%365))/7)),"weeks",int(int(a%365)%7),"Days")