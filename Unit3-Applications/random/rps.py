'''
Mr. Chung
4/19: Rock, Paper, Scissors
'''

import random

u_choice = input('Enter R, P, or S: ')
c_choice = random.choice('RPS')

print('Computer chose', c_choice)

if u_choice == c_choice:
    print('Tie!')
else:
    if u_choice == 'R':
        if c_choice == 'P':
            print('Computer wins!')
        else:
            print('User wins!')
    elif u_choice == 'P':
        if c_choice == 'R':
            print('User wins!')
        else:
            print('Computer wins!')
    else:
        if c_choice == 'R':
            print('Computer wins!')
        else:
            print('User wins!')
