import time

now = time.strftime('%H:%M:%S')
print(now)
h = int(time.strftime('%H'))
print(h)
m = time.strftime('%M')
print(m)
s = time.strftime('%S')
print(s)

"""
In Python, the time() function returns the number of seconds passed since epoch (the point where time begins).

For the Unix system, January 1, 1970, 00:00:00 at UTC is epoch.
"""
# import the time module
import time

# get the current time in seconds since the epoch
seconds = time.time()

print("Seconds since epoch =", seconds)	

# Output: Seconds since epoch = 1672214933.6804628



"""
The time.ctime() function in Python takes seconds passed since epoch as an argument and returns a string representing local time.
"""
# seconds passed since epoch
seconds = 1672215379.5045543

# convert the time in seconds since the epoch to a readable format
local_time = time.ctime(seconds)

print("Local time:", local_time)

if(h < 12 and h >= 4):
    print("Good Morning")
elif(h < 18 and h >= 12):
    print("Good after noon")
elif(h < 21 and h >= 18):
    print("Good evening")
else:
    print("Good night")