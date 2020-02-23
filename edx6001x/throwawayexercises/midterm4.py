def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    products = []
    ans = 0
    for i in range(len(listA)):
        products.append(listA[i] * listB[i])
    for product in products:
        ans += product
    return ans

listA = [1, 2, 3, 4]
listB = [2, 2, 2, 3]
ans = dotProduct(listA, listB)
print(ans)