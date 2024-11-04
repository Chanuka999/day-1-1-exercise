print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("welcome to tresure island")
print("Your mission is find the treasure")

choice1 = input('You are at a crossroad, where do you want to go? Type="left" or "right".\n').lower()


if choice1 == "left":
   choice2 = input('you are come to a lake.there is an island in the lake.Type "wait" to wait for a boat.Type "swim" to swim across\n').lower()
   if choice2 == "wait":
    choice3 =input("you arrive at the island unhared.there is a house with 3 doors.one red one yellow and one blue.which color do do you choose\n").lower()
    if choice3 == "red":
        print("It is a room full of fire.Game over.")
    elif choice3 == "yellow":
        print("you found the treasure!You Win")
    elif choice3 == "blue":
        print("you enter a room of beast.Game over.")
    else:
       print("you choose a door that does not exist.Game over.")
   else:
       print("you got attacked by an angry trout.game over")
else:
    print("You tell into a hole.Game over")
