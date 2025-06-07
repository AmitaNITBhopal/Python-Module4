#Take a score as input and print the grade

print("Please enter your score")
score = int(input())

print("Your grade is")
if score >= 90:
    print("A")

elif score >= 80:
    print("B")

elif score >= 70:
    print("C")

elif score >= 60:
    print("D")

else:
    print("F")