# Text Adventure - start

print("Theres a lottery!")
print("It says:\nLocal Buster Lottery! 600 Million Dollars is on the line!")

# Cast your vote

vote = (input("Cast your vote? (yes or no)\n"))

if vote == "no":
    print("k. bye.")
elif vote == "yes":
    print("You have won 600 million dollars!")
    print("You have recieved powerups!")
    print("20x chance of homocide")
    print("And HIGHER CHANCES OF:\ndrug overdose\nbankruptcy\nkidnapping")

    money = (input("Do you want to take it all out as cash or slowly over time? (cash or time)\n"))

    if money == "time":
        print("You just lost $$ due to annual taxes! - Bankrupt!")
    elif money == "cash":
        print("Good! You managed to avoid losing money")
        print("Someone begged you to donate money")

        donate = (input("Will you donate? (yes or no)\n"))

        if donate == "yes":
            print("Bankrupt! After you said yes, everyone swarmed you and took your money")
        elif donate == "no":
            print("Great! You avoided going bankrupt due to people swarming you after the donation was given.")
        
