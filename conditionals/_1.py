score=input("Enter score: ")
score=int(score)

if score>100:
    print("Invalid score")
elif score>=90:
    print("A")
elif score>=80:
    print("B")
else:
    print("C")