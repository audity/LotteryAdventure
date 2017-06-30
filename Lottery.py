# Text Adventure - start

go_again = True

while go_again == True:
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

        # Cash or time?

        money = (input("Do you want to take it all out as cash or slowly over time? (cash or time)\n"))

        if money == "time":
            print("You just lost $$ due to annual taxes! - Bankrupt!")
        elif money == "cash":
            print("Good! You managed to avoid losing money")
            print("Someone begged you to donate money")

            # Donate or no?

            donate = (input("Will you donate? (yes or no)\n"))

            if donate == "yes":
                print("Bankrupt! After you said yes, everyone swarmed you and took your money")
            elif donate == "no":
                print("Great! You avoided going bankrupt due to people swarming you after the donation was given.")

                # Ant

                Ant = (input("Your second wife has asked you for 100,000 dollars, will you give? (yes / no)\n"))

                if Ant == "yes":
                    print("Oh no! The rest of your family is mad and one of your distant family members kills you due to jealously.")
                    print("YOU DIED")
                elif Ant == "no":
                    print("Good job! Your second family is mad at you, but it's nothing you can't deal with.")
                    print("Rumors say that someone is out to steal your money! ")

                    # Rumors

                    Ru = (input("Do you want to hide your cash in your car (unlikely to find) or your closet (safer)? (car / closet)\n"))

                    if Ru == "car":
                        print("Someone stole your fortune, you lost a lot of cash. - Bankrupt!")
                    elif Ru == "closet":
                        print("It wasn't the smartest place but... no one managed to break into your house!")
                        print("SOMEONE IS APPROACHING...\nIt's a financial advisor and he wants you to hire him on the spot!")

                        # Financial Advisor

                        FA = (input("Do you want to hire him? (yes / no)\n"))

                        if FA == "yes":
                            print("Bad decision! He has scammed you and took all of your cash!")
                        elif FA == "no":
                            print("Good! You avoided getting scamming from the fake financial advisor.")

                            # brother sues

                            print("Your brother finds out about your second family and threatens to expose to your real family if you don't give him 2 million dollars.")
                            brother = (input("Do you give your brother 2 million dollars? (yes / no)\n"))

                            if brother == "yes":
                                print("You make him promise not to tell anyone about the affair but he still tells your wife and she ends up murdering you, R.I.P. Homie")
                            elif brother == "no":
                                print("He exposes you but you change your name and move to another state therefore you're okay.")

                                #death bed

                                print("Your first wife finds you in another state and she shanks you a couple of times and now you're in the hospital laying on your death bed.")
                                print("Your doctor says he could save your life if you go through heart transplant surgery the only catch is the heart is from the black market.")

                                heart = (input("Do you go through the surgery? (yes / no)\n"))

                                if heart == "yes":
                                    print("Looks like the heart was infected and it infected the rest of your body R.I.P Homie")
                                elif heart == "no":
                                    print("You needed that heart to live homie R.I.P")
