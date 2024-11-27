
class Account:
	
	def __init__(self, balance, accNo):
		self.balance = balance
		self.accNo = accNo
	
	def debit(self, amount):
		self.balance -= amount
		print("Rs.", amount, "was debited")
		print("total balance =", self.printBalance())
		
	def credit(self, amount):
		self.balance += amount
		print("Rs.", amount, "was credited")
		print("total balance =", self.printBalance())
		
	def printBalance(self):
		return self.balance
		 

account1 = Account(1000, 108)
account1.debit(100);
account1.credit(100);
print(account1.printBalance()) 
