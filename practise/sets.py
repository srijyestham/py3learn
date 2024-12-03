#sets

#num2 = { 1,2,3,4}
#set2 = {1,2,2,2}

null_set = set()

collection = set()

collection.add(1)
collection.add(1)
collection.add(2)

print(collection) # { 1, 2}

collection.remove(1)
print(collection) 

collection.add("Hello")

tuple1 = (1, 2, 3, 4)
print(type(tuple1))

list1 = [1, 2, 3, 4]
dict1 = {
	"name": "A"
		}

collection.add(tuple1)
print(collection)

#collection.add(list1) # unhashable
print(collection)

#collection.add(dict1) # unhashable
print(collection)


set1 = {1, 2, 3}
set2 = {2, 3, 4}

set3 = set1.union(set2)
print(set3)

set3 = set1.intersection(set2)
print(set3)
