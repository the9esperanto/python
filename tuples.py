# tuples are immutable
# enclosed with ()

a = ("Shree Ram", "Seeta", "Laxaman")
print(type(a))
print(a)


# When we make a tuple with single element then add a comma next to it otherwise the tuple won't be created instead of that the data of data type of that single element will be created.
b = ("Ravana")
print(type(b))
c = ("Narad Muni",)
print(type(c)) 


# Tuple cannot be changed
d = ("Shree Ram", "Hanuman", "Sita", "Laxaman")
# d[0]= "Shurpanakha" 
# This will produce errors
print(d)
d = d[1:2]
print(d)
d = ("Ayodhya Ram")
print(d)