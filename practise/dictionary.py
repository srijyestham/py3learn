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
print(student)
