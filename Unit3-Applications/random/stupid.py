'''
Mr. Chung
4/19: Mr. Chung's awesome dice game
- Roll 5 dice, compute total sum
- Guess whether the next roll's sum will be higher or lower than this one
- Roll again, determine win or lose
'''

import random

rolls = []
total1 = 0
for i in range(5):
    roll = random.randrange(1, 7)
    total1 += roll
    rolls.append(roll)

print('Here are the rolls from Round 1:')
print(rolls)
print('The sum of the Round 1 rolls is:', total1)

u_choice = input('Do you think the next round will be more or less? ')

rolls.clear()
total2 = 0
for i in range(5):
    roll = random.randrange(1, 7)
    total2 += roll
    rolls.append(roll)

print('Here are the rolls from Round 2:')
print(rolls)
print('The sum of the Round 2 rolls is:', total2)

if total1 > total2:
    if u_choice == 'more':
        print('You lose!')
    else:
        print('You win!')
else:
    if u_choice == 'more':
        print('You win!')
    else:
        print('You lose!')







#
