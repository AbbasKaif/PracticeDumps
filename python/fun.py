def add(n1,n2):
	return (n1+n2)
def mul(n1, n2):
	return (n1*n2)
def calc(n1, n2, operator):
	return operator(n1,n2);
print(calc(2,3,mul));