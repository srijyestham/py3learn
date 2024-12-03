info = {
	"name": "A",
	"subjects": ["python", "c", "java"],
	"topics": ("dict", "set"),
	"age": 20,
	"isMember": True,
	12: 16.189,
	12.99: 18.16,
	True: False
}

print(info)
print(info["name"])

info["name"] = "b"

print(info)

info["name2"] = "c"

print(info)


null_dict = {}
print(null_dict)


#nested dictionarys

student = {
	"name": "A",
	"subjects": {
		"Chem": 98,
		"Phy": 99,
		"Math": 100
		},
	"grade": "A+"
}

print(student)

print(student["subjects"])
print(student["subjects"]["Chem"])

print("Student keys", student.keys())
print("As list ",list(student))
print("Total keys", len(student))
print("Length as list", len(list(student)))
print("All Values", student.values())
print("List all key-value pairs", student.items())
print("The above as list", list(student.items()))
print("Accessing above as list")
pairs = list(student.items())
print(pairs[1])
print("get() method")
print(student.get("name")) #1
print(student.get("subjects"))
print("Above can be replicated by below")
print(student["name"]) #2
# the difference is response to errors
# 1 will continue execution in case it 
# is not able to fetch the required
# instead it will output "None"
# in case of 2 it will error and halt the execution flow

# update .update() method
student.update({"class": "10"})
print(student)
# dict itself can be inserted
newDict = {"Books": { "chem", "phy", "math"}}
student.update(newDict)
print(student)
