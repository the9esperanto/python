import random

# Create a program capable of displaying questions to the user like KBC.

question = [
    "______________ is not among the eight principles followed by the Software Code of Ethics and Professional Practice.",
    "Which of the following are CASE tools?",
    "Software patch is defined as ______________",
    "_________ is not a fundamental activity for software processes in software development.",
]

# environment
# emergency
# verification
options = [
    ["PRODUCT", "PUBLIC", "ENVIRONMENT", "PROFESSION"],
    [
        "Emergency Fix",
        "Daily or routine Fix",
        "Required or Critical Fix",
        "None of the mentioned",
    ],
    ["Evolution", "Design and implementation", "Validation", "Verification"],
]

e = random.randrange(1, 3)
print(question[e])

for i in options[e]:
    print("   ", end=" ")
    print(i)

print("\nChoose correct option", end="\n")
x = int(input())
if x < 0 or x > 4:
    print("Selected Wrong option")
    quit()

print(options[e][x])
if e == 0 and x == 2:
    print("Right answer")
elif e == 1 and x == 0:
    print("Right answer")
elif e == 2 and x == 3:
    print("Right answer")
else:
    print("Wrong answer")
