class a:
	def printa(self):
		print("This is class A")
class b(a):
	def printb(self):
		print("This is class B")
class c(b,a):
	def printc(self):
		print("This is class C")
ob=c()
ob.printc()
ob.printb()
ob.printa()