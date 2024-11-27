class Circle:
	def __init__(self, r):
		self.r = r
		
	def area(self):
		return 22 / 7 * self.r * self.r
		
	def perimeter(self):
		return 2 * 22 / 7 * self.r
		
c1 = Circle(108)
print("Area of Cirle with Radius", c1.r, " : ", c1.area())
print("Perimeter of Circle with Radius", c1.r, " : ", c1.perimeter()) 
