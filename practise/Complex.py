'''
class Complex:
	def __init__(self, real, img):
		self.real = real
		self.img = img
		
	def showNumber(self):
		print(self.real, "i +", self.img, "j")
		
	# normal function to add complex numbers	
	def add(self, num2):
		newReal = self.real + num2.real
		newImg = self.img + num2.img
		return Complex(newReal, newImg)
		
		

num1 = Complex(1, 3)
num1.showNumber() # 1i + 3j

num2 = Complex(4, 6)
num2.showNumber()

#num3 = num1 + num2 # results in error as not + yet overloaded
#print(num3)

num3 = num1.add(num2)
print(num3.showNumber())
'''

# to add these complex numbers
# dunder functions are used, operator overloading

# now using dunder function

class Complex:
	def __init__(self, real, img):
		self.real = real
		self.img = img
		
	def showNumber(self):
		print(self.real, "i +", self.img, "j")
		
	# dunder function to add complex numbers	
	def __add__(self, num2):
		newReal = self.real + num2.real
		newImg = self.img + num2.img
		return Complex(newReal, newImg)
		
	# dunder subtract
	def __sub__(self, num2):
		newReal = self.real - num2.real
		newImg = self.real - num2.real
		return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber() # 1i + 3j

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 + num2  # now works
num3.showNumber()

num3 = num1 - num2
num3.showNumber() 
