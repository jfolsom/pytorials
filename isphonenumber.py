
userinput = """
            I am the very 55522222222 of a modern 555-555-5555 and
            cheese 222-555-nope is made of 111-222-3333 ok
            """

print('userinput:')
print(userinput)

def isphonenumber(text):
    if len(text) != 12 and len(text) != 10:
        return False
    for i in text:
        if not i.isdecimal() and i != '-':
            return False
    if len(text) == 12 and text[3] != '-':
        return False
    return True

for i in range(len(userinput)):
    if isphonenumber(userinput[i:i+12]):
        print("Phone number:", userinput[i:i+12])

print('tch. that is all. tch')

    