'''
class Student:
	def __init__(self, phy, chem, math):
		self.phy = phy
		self.chem = chem
		self.math = math
		self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
	
	def calPercentage(self):
		self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

	
stu1 = Student(98, 97, 99)
print(stu1.percentage) # 98

#new marks
stu1.phy = 86
print(stu1.phy) # 86
print(stu1.percentage) #98

stu1.calPercentage()
print(stu1.percentage) # 94
'''

# more proper way is to use decorators
# decorator being property


class Student:
	def __init__(self, phy, chem, math):
		self.phy = phy
		self.chem = chem
		self.math = math
		#self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
	
	'''
	def calPercentage(self):
		self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
	'''
	
	@property
	def percentage(self):
		return str((self.phy + self.chem + self.math) / 3) + "%"
	
stu1 = Student(98, 97, 99)
print(stu1.percentage) # 98
print(stu1.phy) # 98

#new marks
stu1.phy = 86

print(stu1.phy) # 86

print(stu1.percentage) #94

