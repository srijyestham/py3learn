

class Student:
	
	def __init__(self, name, subject1, subject2, subject3):
		self.name = name
		self.subject1 = subject1
		self.subject2 = subject2
		self.subject3 = subject3
		
	@staticmethod # decorator
	def greetings():
		print("hello")
		
	def averageMarks(self):
		average = (self.subject1 + self.subject1 + self.subject1) / 3.0
		print("Name:", self.name, "Average Marks:", average)
		

firstStudent = Student("Didi", 100, 100, 100)
firstStudent.greetings()
firstStudent.averageMarks()

#del firstStudent.greetings
print(firstStudent.greetings())

del firstStudent
print(firstStudent)
