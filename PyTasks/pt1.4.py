#Electricity Bill

bill=0
u=float(input("Enter Units "))
if u>=1 and u<=150:
	bill=u*2.40
elif u>=151 and u<=300:
	bill=(150*2.40)+((u-150)*3.00)
else:
	bill=(150*2.40)+(150*3.00)+((u-300)*3.20)
print (bill)