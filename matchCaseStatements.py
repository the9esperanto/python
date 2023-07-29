import time

x = int(time.strftime("%H"))
print(x)
match x:
    case x if (x < 12 and x >= 4):
        print("Good Morning")
    case x if (x < 18 and x >= 12):
        print("Good Afternoon")
    case x if (x < 21 and x >= 18):
        print("Good evening")
    case _:
        print("Good Night")


# we don't need to use break statement
