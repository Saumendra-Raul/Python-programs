import random
n=random.randint(1,90)
print("I have picked a number between 1 and 90! Try to guess it!\n\n")
diff = int(input("""welcome to number guessing game, Please select difficulty:
1=easy(10 attempts)
2=medium(7 attempts)
3=hard(5 attempts) : """))
if (diff ==  1):
    attempt = 10
elif (diff == 2):
    attempt = 7
elif (diff == 3):
    attempt = 5
else:
    print("invalid input")
    exit()

for i in range(1,attempt+1):
    a= int(input(f"enter guess no {i}:"))
    if (a<n):
        print(f"your guess is too low,you have {attempt-i} guesses left")
    elif(a>n):
        print(f"your guess is too high,you have {attempt-i} guesses left")
    else:
        print(f"your guess was right, the number was {n}")
        break
else:
    print(f"Out of attempts! The number was {n}. Better luck next time!")

    
