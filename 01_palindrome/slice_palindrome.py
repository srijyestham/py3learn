# First Python 3 Project Palindrome

#static build

print("Satyam Shivam Sundram")


#define string below
test_string = "om"

print(test_string)

# inverting a string with slicing

inverted_test_string = test_string[::-1]

# print inverted_test_string
print(inverted_test_string)

#logic to check for palindrome status

if ( test_string == inverted_test_string) :
    print("String is a palindrome")
    
else:
    print("String is not a palindrome")
