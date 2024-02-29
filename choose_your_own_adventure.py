
name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input(
    "You are on a dirt road, it has come to an end. Which way would you like to go - left or right? ").lower()


if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across: ")
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game. ")
    else:
        print("Not a valid option. You lose. ")    
    


elif answer == "right":
    answer = input("You are on a bridge, it looks wobbly, do you want to cross it or held back? ")

    if answer == "back":
        print("You went back and lose. ")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        
        if answer == "yes":
            print("You listened them and follow their advice. You won the gold price. ")
        elif answer == "no":
            print("You ignored them and you are lost in the adventure")
        else:
            print("Not a valid option. You lose. ")    
    else:
        print("Not a valid option. You lose. ")    



else:
    print("Not a valid option. You lose.")

print("Thanks for trying", name)
