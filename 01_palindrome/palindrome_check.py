# Palindrome check by various methods


print("Palindrome Check Program!")

print("----------------------------------------------")



#
##Half String Check
#
#def palindromeCheck(stringArg):
#    print("Beginning Palindrome Check Function")
#    
#    for i in range ( 0,  int(len(stringArg)/2)):
#        #print("Loop Check")
#        if stringArg[i] != stringArg[len(stringArg)-i-1]:
#            return False
#    return True
#    
#    


# Inbuilt Function Method

#def palindromeCheck(stringArg):
#    print("Begin Check!")
#    
#    reverse = ''.join(reversed(testString))
#    print(reverse)
#    
#    if ( testString == reverse):
#        return True
#        
#    return False    
    
#if (palindromeCheck(testString) == True ):
#        print("String is a Palindrome")
#        
#else :
#        print("String is not a Palindrome")
   
   
# Character by Charter Check

    


#emptyString = ''
#
#for i in testString:
#    emptyString = i + emptyString
##    print(i)
##    print(emptyString)
##    print("one loop")
#
#if ( testString == emptyString):
#    print("String is a Palindrome")
#    
#else:
#     print("String is not a Palindrome")
#    

testString = "racecar"

# Testing using Flag

#flag = 1;
#j = -1
#
#for i in testString:
#    if i != testString[j]:
#        flag = 0
#        break
#    j = j - 1
#    
#if (flag == 1):
#    print("String is a Palindrome")
#    
#else:
#    print("String is not a Palindrome")
#    


#Testing using Recursion

def palindromeCheck(testString):
    
    print(testString)
    testString = testString.lower()
    print(testString)
    
    length = len(testString)
    
    if length < 2:
        return True
        
    elif testString[0] == testString[length-1]:
        
        return palindromeCheck(testString[1:length-1])
        
    else:
        return False
        
if palindromeCheck:
    print("String is a Palindrome")
    
else:
    print("String is not a Palindrome")
        

