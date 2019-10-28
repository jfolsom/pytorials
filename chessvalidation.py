# do stuff with dictionaries.
import pprint

# Ask the user to place pieces on the chessboard
# But not right now, because of the break on line 9
chessboard = {'a1': 'wpawn', 'b1': 'wpawn', 'c1': 'wpawn', 'd1': 'wpawn', 'e1': 'wpawn',
              'f1': 'wpawn', 'g1': 'wpawn', 'h1': 'wpawn', 'a2': 'wpawn'}

while True:
    break
    print('What space shall I put the pieace on?')
    print('Enter a value between "1a" and "8h", or enter nothing')
    print('if you are finished placing pieces:')
    space = input()
    print('What piece shall I put on the space?')
    print('Enter a value like "wkinght" or "bbishop",')
    print('Or enter nothing if finished:')
    piece = input()
    if space == '':
        break
    else:
        chessboard[space] = piece

numbers = []
spaces = []
letters = 'abcdefgh'
validpieces = (['wking', 'wqueen', 'wrook', 'wbishop', 'wknight', 'wpawn'] +
          ['bking', 'bqueen', 'brook', 'bbishop', 'bknight', 'bpawn'])

# Create the list of valid spaces
for i in range(1, 9):
    numbers.append(str(i))
for i in range(0, 8):
    for j in range(0, 8):
        spaces.append(letters[i] + numbers[j])

# Check that list agains the spaces the user entered
eachspacevalid = []
for placed_space in chessboard.keys():
    eachspacevalid.append(placed_space in spaces)
validspaces = not False in eachspacevalid
# All the spaces were valied if False was not in eachspacevalid
print('Spaces are valid? ', validspaces)

# Check the list of pieces the user placed against the list of valid pieces
eachpiecevalid = []
for placedpiece in chessboard.values():
    eachpiecevalid.append(placedpiece in validpieces)
validpieces = not False in eachpiecevalid
print('Pieces are valid? ', validpieces)


# Check for duplicate pieces
# This should be changed as it will flag two bishops or two rooks as invalid
def comparethis(this_piece):
    # Recieve a placed piece and check the list of placed pieces
    # to find out if the received piece has any duplicates.
    count = 0
    for tothatpiece in chessboard.values():
        if this_piece == tothatpiece:
            count += 1
    if count == 1 or this_piece[1:5] == 'pawn':
        unique = True
    else:
        unique = False
    return unique
# Now do that for all of the pieces, and store the results for each
# in the list uniquepieces
uniquepieces = []
for piece in chessboard.values():
    uniquepieces.append(comparethis(piece))
# If every piece in the list is unique, then the pieces are unique.
if not False in uniquepieces:
    piecesareunique = True
print('Pieces are unique? ', piecesareunique)

# Report True if there are two kings
twokings = ('wking' in chessboard) and ('bking' in chessboard)
print('Are there two kings? ', twokings)

# Report True if there are less than 16 pieces on each side
whitepieces = {}
blackpieces = {}
for space, piece in chessboard.items():
    if chessboard[space][0] == 'w':
        whitepieces[space] = piece
    elif chessboard[space][0] == 'b':
        blackpieces[space] = piece
    else:
        print('How did we get here? 01')
righnumberofpieces = len(whitepieces) <= 16 and len(blackpieces) <= 16
print('Does each player have 16 pieces or less? ', righnumberofpieces)

# Report True if each player has lees than 8 pawns

wpawns = 0
bpawns = 0
for piece in chessboard.values():
    if piece == 'wpawn':
        wpawns += 1
    elif piece == 'bpawn':
        bpawns += 1
print(wpawns)
print(bpawns)
rightnumberofpawns = wpawns <= 8 and bpawns <= 8
print('Do both players have a legitimate number of pawns? ', rightnumberofpawns)


