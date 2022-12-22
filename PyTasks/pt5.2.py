class Rectangle:
	def __init__(self,l,w):
		self.l,self.w=l,w
	def rectarea(self):
		print("Area of Rectangle is",(self.l*self.w),"sq. units")
	def rectperi(self):
		print("Perimeter of Rectangle is",(2*(self.l+self.w)),"units")
l=float(input("Enter Length of the Rectangle: "))
w=float(input("Enter Width of the Rectangle: "))
r=Rectangle(l,w)
r.rectarea()
r.rectperi()