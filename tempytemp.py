#! Python3
# Draw some squares


edge = "+----+----"
row = "/    /    "
for j in range(4):
    print(edge, edge, edge, edge, '+', sep="")
    for i in range(4):
        print(row, row, row, row, '/', sep="")
print(edge, edge, edge, edge, '+', sep="")


