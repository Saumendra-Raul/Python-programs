import time
score =0
print("""welcome to my general quiz :)
try to answer all the questions below correctly!\n\n""")
start=time.time()
ques = [
    ["What is the capital of India?\n(a) Delhi\n(b) Mumbai\n(c) Kolkata", "a"],
    ["Python is a _____ language.\n(a) compiled\n(b) interpreted", "b"],
    ["Which planet is known as Red Planet?\n(a) Mars\n(b) Venus", "a"],
    ["Which year did India get independence?\n(a) 1947\n(b) 1950", "a"],
    ["HTML is used for?\n(a) Designing webpages\n(b) Data analysis", "a"]
]

for i in ques:
    ans= input(i[0] + "\nYour Answer:")
    if ans.lower()==i[1]:
        print("Saabash londe!\n")
        score+=1
    else :
        print("Padhke aa\n")
end=time.time()
total=end-start

print(f"""quiz khatam, aaj ki dehaadi : {score}/{len(ques)}
percentage: {score/len(ques)*100}""")
if score == 5:
    print("Touch grass! (jk congrats)")
elif score in [3, 4]:
    print("Almost there champ, make your mama proud")
elif score in [1, 2]:
    print("Get better bozo!")
elif score == 0:
    print("huh?")

print(f"\n\nYou completed the quiz in {int(total)} seconds!")
if total <= 5 and score == 5:
    print("lucky spammer, or god")
elif total <= 5 and score < 3:
    print("spamming is bad")
elif total <= 5 and score == 0:
    print("cat jumped on keyboard?")
elif total <= 30 and total > 5:
    print("speedy :)")
elif total > 100:
    print("fell asleep?")
else:
    print("good speed 👍")
