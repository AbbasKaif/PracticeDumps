class interest:
	def __init__(self,p,n,r):
		self.p,self.n,self.r=p,n,r
	def simpleinterest(self):
		print("Simple Interest=",(self.p*self.n*self.r*0.01))
print("Calculation of Simple Interest.")
p=float(input("Enter Principle: "))
n=float(input("Enter Duration(in years): "))
r=float(input("Enter Rate of Interest(p.a): "))
i=interest(p,n,r)
i.simpleinterest()