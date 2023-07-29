"""
1. strings are immutable.
2. any method on string takes a copy of the object.
3.string.upper will convert the string to an upper case
4.string.lower will convert the string to lower case
5. string.rstrip("character") will strip the trailing characters of string 
6.string.replace("character/alphabets", new character/alphabets") will replace the existing specified alphabets in string with new ones
7. string.split splits the string at the given alphabet and returns a list of items
8.string.capitalize capitalizes the first character of the word and turns rest all the characters to lower case
9.string.center center aligns the string by adding the number of spaces mentioned in parenthesis
10. string.count counts the total number of a particular set of characters in a string
11. string.endswith checks whether a string ends with the specific characters
12.string.find finds the first occurrence of a given value and return the index value of the position of that occurrence
13.string.index finds the occurrence of a given value and returns the index value of the position however, if it is unable to find it will give an error causing the program to exit
14.string.isalnum checks to find if string is alphanumeric and returns true or false
15.string.isalpha checks if there are any numbers in the string
16.string.islower checks if there are only lower aphabets in the string
17. string.isprintable checks if all the characters are printable in the string(non printable characters e.g \n)
18 string.isspace checks if any space bar has been used in the string
19.string.istitle The istitile() returns True only if the first letter of each word of the string is capitalized, else False
20. string.isupper checks if all characters are uppercase in a string
21. string.startswith checks if a string starts with a given value
22. string.swapcase convert uppercase to lowercase and vice versa in a string
23.string.title converts first character of all the words in the sentence to capital
"""


# A method is a function that “belongs to” an object.
# Strings are immutable
# Strings cannot be changed inplace.
a = "Ram"
a = "Hardeek"
print(a)

b = "Shatrugan"
# b[1] = T
# This will produce error
print(b.upper())
# This will not produce changes in the original string but make a copy
print(b)



# CONVERT TO UPPER CASE
c = "Bharat"
c = c.upper()
print(c)
d = "Sumantra"
print(d.upper())
print(d)

# CONVERT TO LOWER CASE
e = "Kaikeyi"
print(e.lower())
f = "Ahalya"
f = f.lower()
print(f)

# REMOVES TRAILING CHARACTERS
g = "Jai Hanuman!!!!!"
print(g.rstrip("!"))
print(g)
h = "Janaki!!!"
h = h.rstrip("!")
print(h)

# REPLACE ALL OCCURENCES OF A STRING WITH ANOTHER STRING

i = "Jai Shree Ram!!!"
print(i.replace("Shree Ram", "Hanuman"))
print(i)
i = i.replace("Shree Ram", "Siya Ram")
print(i)

# SPLITS AT THE GIVEN INSTANCE AND RETURNS THE SEPARATED STRINGS AS LIST ITEMS

j = "Raghupati Raghav Raja Ram"
print(j.split(" "))
k = "Bhadra Girishwara Sitaram Bhagat Janpriya Sitaram"
k = k.split(" ")
print(k)


# Capitalize turns only the first character of string to uppercase and rest to lower case. The string has no effect if the first character is already upper.

l = "shree ram"
m = "Vashishta Muni"
n = "shree Parshuram"

print(l.capitalize())
print(m.capitalize())
print(n.capitalize())


# Center method aligns the string to the center according to given parameter

o = "Jai Shiv Shankar"
print(o)
print(o.center(10))
print(len(o))
print(len(o.center(10)))

# The size does not remains same.



# Count return the number of occurences of a string

p = "Har Har Mahadev"
print(p.count("Har"))
# It is case sensitive


# endswith tells us if a string ends with a specific string

q = "Sita Urmila Mandavi Shrutakirti!!!"
print(q.endswith("!!"))
print(q.endswith("!!!!"))
