# adding new element at the end of a list
# append

a = ["Shree Ram", "Laxman", "Bharat", "Shatrughna"]
print(a)
a.append("Hanuman")
a.append("Guha")
print(a)


# sorting the list

b = [1, 100, 9, 0, 8, 45, 39, 89]
print(b)
b.sort()
print(b)
a.sort()
print(a)

# reverse the list

c = [999, 99, 9]
print(c)
c.reverse()
print(c)

# gives index of the first occurence of the item

d = ["Dandakaranya", "Ayodhya", "Mithila"]
print(d.index("Mithila"))


# count()
e = ["Ram", "Ram", "Ram"]
print(e.count("Ram"))


# copy()
f = [
    "Shree Ram",
    "Dashrath Nandan",
    "Siyavar",
    "Hanuman Priya",
    "Mahabahu",
    "Kaushalya Putra",
]

# without copy it is like two names but same space
g = f
g[0] = "Shree Ramchandra"
print(f)
print(g)

# with pointer the original does not gets changed
h = f.copy()
h[0] = "Shree Ram"
print(h)
print(f)


# insert method
# This method inserts the new item at the index and the item present at the index before insertion moves to next index

i = ["Rishi Agustya", "Rishi Vashishtha", "Rishi Vishwamitra"]
i.insert(1, "Rishi Bharadwaj")
print(i)


# extend method
# extend method adds an entire collection datatype(tuple, list, set, dictionary) to existing list.

j = ["Shree Ram", "Laxaman", "Bharat", "Shatrughna"]
k = ["Kaushalya", "Kaikeyi", "Sumitra"]
print(j)
j.extend(k)
print(j)
print(k)

k.extend(j[0][2])
print(k)
