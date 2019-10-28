import random

coinflips = []
flipsnumber = 10000
streaks = 0
sequences = 0
# Flip a coin 10000 times
for i in range(flipsnumber-1):
    coinflips.append(random.randint(0,1))

for i in range(flipsnumber-6):
    if coinflips[i:(i+6)] == [0, 0, 0, 0, 0, 0] or \
       coinflips[i:(i+6)] == [1, 1, 1, 1, 1, 1]:
        streaks += 1
    sequences += 1
percentchance = str(round((streaks/sequences)*100, 1))
print(streaks, 'streaks out of', sequences)
print(percentchance)
