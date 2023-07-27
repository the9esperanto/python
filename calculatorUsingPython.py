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
print("Enter second operator \n")
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



