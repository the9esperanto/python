# a = 2
# b = 3
# gmean = (a*b)/(a+b)
# print(gmean)

# Writing a function

def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

calculateGmean(9,8)


def islesser(a, b):
    pass

islesser(2, 3)

def islesser(a, b):
    print(min(a,b))

islesser(2, 3)


# Function arguments
def average(a, b):
    print("The average is" , ((a+b)/2))
# Here a and b are required arguments

average(7, 9)

# Default arguments
def sum(a = 1, b = 2):
    print("The sum of", a ,"and", b, "is", a+b)
sum()
sum(6,7)
sum(5)
sum(b=4)


# Variable length arguments (tuple)

def average(*numbers):
    sum = 0
    print(type(numbers))
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum/len(numbers))

average(3, 8, 2, 9, 5)


# Return 

def average(*numbers):
    sum = 0
    print(type(numbers))
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

c = average(3, 8, 2, 9, 5)
print(c)