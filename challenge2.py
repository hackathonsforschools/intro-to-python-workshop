## CHALLENGE ##

print('''
Choose any of the three following ice cream flavours...
1. Chocolate
2. Strawberry
3. Vanilla

If you enter none of the above, you will be given mint.
''')

choice = int(input("Pick your choice (enter number 1-3) > "))

if (choice == 1):
    flavour = "chocolate"
elif (choice == 2):
    flavour = "strawberry"
elif (choice == 3):
    flavour = "vanilla"
else:
    flavour = "mint"

print("You chose {} flavoured ice cream.").format(flavour)

## EXTENSION ##

print('''
Choose any two of the three following ice cream flavours...
1. Chocolate
2. Strawberry
3. Vanilla

If you enter only one or none, you will be given mint.
''')

options = ["chocolate", "strawberry", "vanilla"]

choices = input("Pick your choice (enter numbers 1-3) > ").split('&')

giveMint = False

if len(choices) < 2:
  giveMint = True

if giveMint:
  print("You chose mint flavoured ice cream.")
else:
  firstChoice = options[int(choices[0])-1] # must subtract 1 as indexing starts at 0
  secondChoice = options[int(choices[1])-1]
  print("You chose {} and {} flavoured ice cream.").format(firstChoice, secondChoice)