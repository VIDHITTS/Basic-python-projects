import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#0-rock
#1-scissors
#2-paper
computer_choice=random.randint(0,2)
user_choice=int(input('what do you choose? Type 0 for rock ,1 scissors or 2 for paper'))
print('Your choice:')
if user_choice==0:
    print(rock)
elif user_choice==1:
    print(scissors)
elif user_choice == 2:
    print(paper)
else:
    print('Invalid input')
print()
print('Computer chose:')
if computer_choice==0:
    print(rock)
elif computer_choice==1:
    print(scissors)
else:
    print(paper)
print()
print('Computer Chose')
if user_choice==0 and computer_choice==1:
    print('You Win')
elif user_choice==0 and computer_choice==2:
    print('You Lose')
elif user_choice==1 and computer_choice==0:
    print('You Lose')
elif user_choice==1 and computer_choice==2:
    print('You Win')
elif user_choice==2 and computer_choice==0:
    print('You Win')
elif user_choice==2 and computer_choice==1:
    print('You Lose')
elif user_choice==computer_choice:
    print('Draw')
else:
    print('Invalid input')










