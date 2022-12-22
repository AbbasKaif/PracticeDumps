def getMagicValue(n,a):
    ls = a
    lp = []
    for i in ls:
        lp.append(i)
    lp.sort()
    gs, bs = 0, 0
    for item in range(len(ls)):
        if(ls[item] == lp[item]):
            gs = gs + ls[item]
        else:
            bs = bs + ls[item]
    return(gs-bs)
	
n = int(input())
a = list(map(int, input().split()))

out_ = getMagicValue(n,a)
print (out_)
