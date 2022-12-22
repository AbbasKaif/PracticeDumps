#Salary

bsal=float(input("Enter Basic Salary "))
if bsal>=1 and bsal<=4000:
	print("Salary=",(bsal+0.1*bsal+0.5*bsal))
elif bsal>=4001 and bsal<=8000:
	print("Salary=",(bsal+0.2*bsal+0.6*bsal))
elif bsal>=8001 and bsal<=12000:
	print("Salary=",(bsal+0.25*bsal+0.7*bsal))
else:
	print("Salary=",(bsal+0.30*bsal+0.8*bsal))