#recursion

def show(n):
	if (n == 0):
		return
	print(n)
	show(n-1)
	print("end")

show(4)


# recursive funciton to calculate sum of first n natural numbers

def sumOfNums(n):
	if (n ==0):
		return 0
	else:
		return sumOfNums(n-1) + n
		
print(sumOfNums(4))

print('''

# recursive function to print all elements in a list
list1 = [1, 2, 3, 4, "a", "b"]
''')

list1 = [1, 2, 3, 4, "a", "b"]
print(list1)

def listRecurser(list1, index):
	if (index == len(list1)):
		return
	print(list1[index])
	listRecurser(list1, index + 1)

listRecurser(list1, 0)
