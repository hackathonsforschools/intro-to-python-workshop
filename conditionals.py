## STEP 1 ##

print(True and False) # False - it's true if both are true, and false otherwise

print(True or False) # True - it's true if either of them is true

print(not True) # False - the opposite of what 'not' is being applied to

print(not False) # True

print(True == True) # True - it's true if the first is equivalent to the second

print(True == False) # False

print('a' == 'a') # True

## REMEMBER: = is for assignment - assigning new variables. == is for comparison! (checking equivalence of 2 values)

## STEP 2 ##

hour = int(input("Enter the hour: ")) # converts string input to int

if hour <= 12:
    print("Good morning!")
if (hour >= 12):
    print("Good afternoon!")


## STEP 3 ##

hour = int(input("Enter the hour: "))

if hour <= 12:
    print("Good morning!")
elif (hour > 12 and hour <= 18):
    print("Good afternoon!")
elif (hour > 18):
    print("Good evening!")


## STEP 4 ##

hour = int(input("Enter the hour: "))

if (hour >= 0 and hour <= 12):
    print("Good morning!")
elif (hour > 12 and hour <= 18):
    print("Good afternoon!")
elif (hour > 18 and hour <= 23):
    print("Good evening!")
else:
    print("Please enter an integer in range 0-23!")