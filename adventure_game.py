name = input("type your name: ")
print("welcome " + name + " to this adventure")

answer = input("You are on a dirt road. It has come to an end and you can go left or right. Which way do you want to "
               "go?").lower()
if answer == 'left':
    answer = input("You've reached a river. You can either walk around it or swim across. Type walk to walk or swim to "
                   "swim across")
    if answer == 'swim':
        print("You were eaten by an alligator. Game over!")
    elif answer == 'walk':
        input("You walked for many miles and ran out of water. Do you drink your own urine or drink from the strange "
              "plants around you? type urine or plants ")
        if answer == "urine":
            print("You got sick from drinking urine and die. Game over!")
        elif answer == "plants":
            print("You get sick from the plants and die painfully. Game over!")
    else:
        print("Invalid choice")

elif answer == 'right':
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross it or go under it? Type cross to cross "
                   "it and under to go under it")
    if answer == 'cross':
        print("The bridge collapses and you fall to your death. Game over!!")
    elif answer == 'under':
        answer = input("You encounter a mad troll do you fight or try to trick him? type fight to fight or trick to "
                       "trick")
        if answer == "fight":
            print("You try to fight the troll and die a horrible painful death. Game over!")

        elif answer == "trick":
            print("You successfully trick the troll into killing itself and collect it's treasure. YOU WIN!!")
else:
    print("You have to pick left or right")

print("Thank you for playing",name," take care")
