# while/continue practice

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe.  What\'s the dealeo?')
    password = input()
    if password == 'swordfish':
        break
print('Welcome home.')

