# Guessing game
number=5
i=1
while i<=5:
    enter=int(input("enter any number from 1 to 10\n"))
    if enter==number:
        print("correct")
        break
    else:
        print("wrong")
    i=i+1
if i==6:
    print("you are unable to guess number")
