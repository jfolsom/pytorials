# playing with lists

def receive_integer():

    receivednumber = -1
    while receivednumber < 1:
        try:
            print('Enter a positive integer:')
            receivednumber = int(float(input()))
            if not receivednumber > 0:
                print('That number is not positive.')
        except ValueError:
            print('That is not an integer.')
            continue
    print('Success:', receivednumber)
    return receivednumber

def letsmakealist(listlength):
    receivedlist = []
    for i in range(listlength):
        print('Enter list item:')
        receivedlist.append(input())
    return receivedlist

completelist = letsmakealist(receive_integer())

print(completelist)
# Receive a positive integer, request that many list items,
# then display that list.

print('Which item do you want?')
receivedindex = receive_integer()
print(completelist[receivedindex])


while True:
    print('Which item do you want to find?')
    target = input()
    try:
        targetindex = completelist.index(target)
        break
    except ValueError:
        print('That\'s not in the list')
        continue
print(targetindex)

print('Okay, lets change it up a bit.')
print('Which item do you want to change?')
itemtoswitch = receive_integer()
while True:
    print('What should we put in it\'s place?')
    replacement = input()
    try:
        completelist[itemtoswitch] = replacement
        break
    except IndexError:
        print('The list isn\'t that long. Try again:')
        itemtoswith = receive_integer()
        continue
print('Now the list looks like this:')
print(completelist)



