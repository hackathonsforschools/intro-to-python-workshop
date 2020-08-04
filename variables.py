### STEP 1 ###

name = "Robert"

print(name)

# ERROR: --- scope!!

print(name) 

name = "Robert"

### STEP 2 ###

username = "cooldog123" # Say we have a variable called 'username' with the value being the string "cooldog123"

message = "Hello {}, welcome to my cool Python program!".format(username) # Either this way - where we put curly braces is placeholder for unknown
print(message)

# # OR if we have more variables

adjective = "awesome"
message = "Hello {}, welcome to my {} Python program!".format(username, adjective)
print(message)

#  # Note, the order within .format() tells Python what order to format the string in, i.e. which word comes first (username then adjective)
#  # To avoid this, we can use identifiers (for placeholders) inside the curly braces as follows:

message = "Hello {usernameString}, welcome to my {adjectiveString} Python program!".format(adjectiveString=adjective, usernameString=username)
print(message)