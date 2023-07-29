"""
+ add
- subtract
* multiply
/ division
% modulus
// floor ZeroDivisionError
** exponential 5**3 = 5^3
"""

print("Enter first operand \n")
a = int(input())
# input(a)
print("Enter second operand \n")
b = int(input())
# input(b)
print("Enter operator \n")
c = str(input())
# input(c)
if(c == "+"):
    print(a+b)


if(c == "-"):
    print(a-b)


if(c == "*"):
    print(a*b)

if(c == "/"):
    print(a/b)

if(c == "%"):
    print(a%b)

if(c == "//"):
    print(a//b)

if(c == "**"):
    print(a**b)



# input() converts everything into string. We need to typecast it before using it.

"""
python 2
-> raw_input() - it will take any type of data and returns it as string value
-> input() - it will take any type of data and treat it accordingly won't change

to make raw_input() behave like input() we write eval(raw_input)
""" 

# n = raw_input() this does not work in python 3

"""
python 3
-> input() - it will behave like raw_input from python2
so we use eval(input())
"""
