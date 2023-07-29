a = "Shree Ram"
b = 'Shree Raghav'
# We can make a string with double or sigle quotes.
print("Jai", a)
print('Hanuman said,"Jai Shree Ram"')

# We cannot start a string on one line and end it on another as the interpreter will check for the ending quotes on the same line and when it does not find it, it shows EOL error.

example = """
So like comments we can write 
that in triple quotes.
"""
print (example)

# What's the difference between multi line string and nultiline comment?

#indexing of string starts from 0
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])
print(a[8])

# It is like an array of characters but not exactly array of characters

# Accesing all the characters at a time with looping through the strings
for i in b:
    print(i)


# String slicing

z = "Shree Ram, Laxman, Bharat, Shatrugan"
print(len(z))
print(z[0:36])
print(z[0:36:3])
y = "12345"
print(y[0:0])
# (start, stop, step)
# the index of a string's last character is the length of the string minus 1
# in slicing if we put [2,4] we won't access 4th index


# Negative Slicing

print(y[0:-1])
# This basically is print(y[0:(len(y)-1)])

print(y[-1:-2])
#This will print nothing because it does not go in reverse
