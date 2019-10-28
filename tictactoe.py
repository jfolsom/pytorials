theboard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])

printboard(theboard)

turn = 'X'

for i in range(9):
    printboard(theboard)
    print('It is ' + turn + '\'s turn. Move on which space?')
    print('enter something like "top-L" or "mid-M" or "bot-R".')
    move = input()
    theboard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printboard(theboard)
