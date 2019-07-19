hifi=int(input())
f=list(map(int,input().split()))
ssa=[]
rrr=[]
for i in f:
    if i%2==0:
        ssa.append(i)
    else:
        rrr.append(i)
if len(ssa)==1:
    print(*ssa)
else:
    print(*rrr)
