class Order:
	def __init__(self, item, price):
		self.item = item
		self.price = price
		
	def __gt__(self, order2Obj): # order2Obj reference is this place only
		return self.price > order2Obj.price
		
order1Obj = Order("Roti", 10)
order2Obj = Order("Pizza", 20)
order3Obj = Order("Idli", 30)

print(order1Obj > order2Obj)
print(order2Obj > order3Obj)
print(order3Obj > order2Obj)
		
