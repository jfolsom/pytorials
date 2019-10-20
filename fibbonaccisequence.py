# Fibbonacci

first_number = 1
second_number = 1

while first_number < 10000:
    hold_second_number = second_number
    second_number = first_number + second_number
    first_number = hold_second_number
    print(str(second_number))

