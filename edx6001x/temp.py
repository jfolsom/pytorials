def fancy_divide(list_of_numbers, index):
    try:
        print('1')
        raise Exception("0")
        print('2')
    finally:
        print('3')
        denom = list_of_numbers[index]
        print('4')
        for i in range(len(list_of_numbers)):
            print('5', i)
            list_of_numbers[i] /= denom
            print('6')
        print('7')