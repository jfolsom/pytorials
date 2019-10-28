# counting characters
import pprint

message = ('It was a bright cold day in April, '
            'and the clocks were striking thirteen.')

print(message)

charactercount = {}

for character in message:
    charactercount.setdefault(character, 0)
    charactercount[character] += 1

pprint.pprint(charactercount)
