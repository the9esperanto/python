# list are ordered collection of data collection
# separated by commas
# enclosed by []


l = [3, 5, 6]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])

m = [3, 5, "Hari", True]
for x in m:
    print(x)


# To check if an item is present in a list

if 5 in m:
    print("Present")
else:
    print("Absent")


if "Har" in "Hardeek" and "Hari":
    print("Yes")