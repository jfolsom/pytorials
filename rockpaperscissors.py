# Play rock paper scissors
print('ROCK, PAPER, SCISSORS')

# Set initial variables
wins = 0
losses = 0
ties = 0
win_text = 'You win!'
loss_text = 'Heh, this round is MINE.'
tie_text = 'A tie.'

import sys
import random

while True:
    print(wins, ' Wins, ',losses, ' Losses, ', ties, ' Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    user_move = input()
    my_move = random.randint(1, 3)     #1 for rock, 2 for paper, 3 for scissors

    # If user enters q, say goodbye then quit.
    if user_move == 'q':
        if losses > wins:
            print('I won! Better luck next time.')
        elif wins > losses:
            print('You beat me!  Next time I will throw more rock.')
        elif wins == losses:
            print('It\'s a tie! We\'ll settle this next time.')
        sys.exit()
    # Name the users move.
    if user_move == 'r':
        u_move_name = 'ROCK'
    elif user_move == 'p':
        u_move_name = 'PAPER'
    elif user_move == 's':
        u_move_name = 'SCISSORS'
    else:
        print('Wrong answer, bud.  Enter a move.')
        continue
    # Translate my move to string and name it.
    if my_move == 1:
        my_move = 'r'
        my_move_name = 'ROCK'
    elif my_move == 2:
        my_move = 'p'
        my_move_name = "PAPER"
    elif my_move == 3:
        my_move = 's'
        my_move_name = "SCISSORS"
    else:
        print('Wrong answer, bud.  Enter a move.')
        continue

    # Figure out who won, set result text, keep score.
    if my_move == 'r':
        if user_move == 'r':
            result = tie_text
            ties = ties + 1
        elif user_move == 'p':
            result = win_text
            wins = wins + 1
        elif user_move == 's':
            losses = losses + 1
            result = 'Good old rock.  Nothing beats rock.'
        else:
            print('How did we get here? 01')
            sys.exit()
    elif my_move == 'p':
        if user_move == 'r':
            result = loss_text
            losses = losses + 1
        elif user_move == 'p':
            result = tie_text
            ties = ties + 1
        elif   user_move == 's':
            result = win_text
            wins = wins + 1
        else:
            print('How did we get here? 02')
            sys.exit()
    elif my_move == 's':
        if user_move == 'r':
            result = win_text
            wins = wins + 1
        elif user_move == 'p':
            result = loss_text
            losses = losses+1
        elif user_move == 's':
            result = tie_text
        else:
            print('How did we get here? 03')
            sys.exit()
    else:
        print('How did we get here? 04')
    #Display Results
    print(u_move_name, ' versus...')
    print(my_move_name)
    print(result)


