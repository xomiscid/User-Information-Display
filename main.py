#An user information display

print("== WELCOME :) ==")
print()
print("Please enter your informations below !")
print()
#Ask for user informations 
first_name = input("Enter your first name :")
name = input("Enter your name :")

#Ask for the user's age and handle the case where they enter something other than a number
try:
 age = int(input("Enter your age :"))
except ValueError:
 print("Error: Please enter a valid number")
 age = int(input("Enter your age :"))
 
city = input("Enter your city name :")

print()

#Display user informations
print("== Display : ==")
print()
print(f"Your first name is : {first_name}")
print(f"Your name is : {name}")
print(f"Your age is : {age} yo")
print(f"Your city is : {city}")
print()
print(f"Thank you {name} ;)")
