# Exercise: rewrite the dictionary "switch" with if/elif/else.
# For a digit 0-9 print "Entered <digit>", otherwise print "Invalid number!"

number = input("Dial a number: ")

if len(number) == 1 and number in "0123456789":
    print("Entered " + number)
else:
    print("Invalid number!")
