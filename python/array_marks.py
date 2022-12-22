n = int(input())
ls = list(map(int, input().split(' ')[:n]))
ql = []
for i in range(len(ls)-1):
    count = 0
    for j in range(len(ls)-1):
        if(i >= ls[j]):
            count = count + 1
            print(count, end=" ")
    print()
    if(count == len(ls)):
        ql.append(ls[i])
print(ql)