## STEP 1 ##

## INSTEAD OF: 
x = 2
y = 6
z = 1

numberSum = x + y + z

print(numberSum)

## DO:

x = 2
y = 6
z = 1

def sumOfThree(a, b, c):
    numberSum = a+b+c
    print(numberSum)

sumOfThree(x, y, z) # here we're "calling" the sumOfThree function
sumOfThree(5, 10, 20) # can pass it direct values instead of variables
# BUT... YOU MUST DECLARE A FUNCTION BEFORE CALLING
# REMEMBER ABOUT VARIABLE SCOPE - IT'S THE SAME - JUST LIKE YOU CAN'T USE A VARIABLE BEFORE DECLARING IT

## STEP 2 ##
print(numberSum) # numberSum's scope was only inside the function - it doesn't exist anymore!

## STEP 3 ##

x = 2
y = 6
z = 1

def sumOfThree(a, b, c):
    numberSum = a+b+c
    return numberSum

result = sumOfThree(x, y, z) # here we're assigning the result of the function to the variable "result"
print(result) # without this, nothing will happen