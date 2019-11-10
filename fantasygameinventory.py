# Display a fantasy game inventory nicely

slots = 'abcdefgh'

inventory = {
            'arrow': 12,
            'monkey': 1,
            'babygirl': 1,
            'potion of cure malady': 2,
            'terrigible': 1,
            'torch': 12,
            'ration': 4}

total = 0

print('Inventory:')

for item, count in inventory.items():
    print(count, end=' ')
    if count == 1:
        print(item)
    else:
        print(item, 's', sep='')
    total = total + count

print('Total number of items: ', total)
