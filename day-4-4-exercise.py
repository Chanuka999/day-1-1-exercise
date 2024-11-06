import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
'''

Paper = '''

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
'''

Scissors ='''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
'''
#print(rock,Paper,Scissors)
user_choice = input("what do you choice Type 0 for rock,1 for paper or 2 for scisser \n")
computer_choice = random.randint(0,2)
print(f"computer choice {computer_choice}")

if user_choice >= 3 or user_choice < 0:
     print("You type in invalid number,you lose")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice == 0 and user_choice ==2:
    print("you lose")
elif computer_choice > user_choice:
    print("you lose")
elif computer_choice > user_choice:
    print("you win")
elif user_choice == computer_choice:
    print("ïts drow")

   
