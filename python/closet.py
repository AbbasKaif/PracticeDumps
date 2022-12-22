def Solve(N, A):
    min_val, idx = min([(abs(val), idx) for (idx, val) in enumerate(A)])
    return(min_val)
N = int(input())
A = list(map(int, input().split()))
out_ = Solve(N, A)
print(out_)