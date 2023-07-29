# Indentation is important in python
# We don't use curly braces but use spaces to indicate the body

# if
b = 6
if b == 6:
    print("b is equal to 6")


# if-else
a = int(input("Enter your age\n"))
print("Your age is", a)

if a >= 18:
    print("You can drive")
else:
    print("You cannot drive")


# if-else-elif
god = "Ram"
weapon = "Sharnga"

if god == "Ram" and weapon == "Sharnga":
    print("Jai Shree Ram")
elif god == "Ram" and weapon != "Sharnga":
    print("Sharnga is the weapon")
elif god != "Ram" and weapon == "Sharnga":
    print(
        "veda vedye pare pumsi jate dasharathatmaje |vedah prachetasadasid sakshad ramayanatmana ||"
    )
else:
    print("Shree Ram, Jai Ram, Jai Jai Ram")


# Nested if Statements

num = 18
if num < 0:
    print("Number is negative")
elif num > 0:
    if num <= 10:
        print("Number is between 1-10")
    else:
        print("Number is greater than 10")
else:
    print("Number is zero")
