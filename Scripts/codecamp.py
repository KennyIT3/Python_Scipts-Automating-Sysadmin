for row in range(1,11):
    for column in range(1,row+1):
        print('{:3}'.format(column),end="")
        # print(column,end="")
    print()

numbers = [-5,8,12,0,3,23,24]

pos = []
neg = []

for number in numbers:
    if number > 0:
        pos.append(number)
    else:
        neg.append(number)
print(pos)
print(neg)