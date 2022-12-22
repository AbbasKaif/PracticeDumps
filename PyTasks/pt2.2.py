print("\n")
print("Program to generate the series of prime numbers in range 1 – 100.\n")
for k in range(1,101):
    n,c,i=k,0,1
    while(i<=n):
        if(n%i==0):
            c=c+1
        i+=1
    if(c==2):
        print(k,end=" ")
print("\n")