print("Welcome to G.K. quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Who is the only cricketer in the world to score 100 international centuries? ")
if answer.lower() == "sachin tendulkar":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("Most popular framework of python? ")
if answer.lower() == "django":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("Who discovered number '0'? ")
if answer.lower() == "aryabhatta":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("Who is the founder of Microsoft? ")
if answer.lower() == "bill gates":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("Tell me about the total number of Tirthankars in every time cycle according to Jainism ")
if answer.lower() == "24":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


print("You did " + str(score) + " questions correct!")

print("You got " + str((score / 5) * 100) + "%.")
