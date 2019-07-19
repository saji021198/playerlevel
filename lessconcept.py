f=int(input())
g=list(map(int,input().split()))
g=sorted(g)
count=0
for i in range (0,f):
    for j in range(1,f):
        if(g[i]<g[j]):
            count=count+1
print(count)


