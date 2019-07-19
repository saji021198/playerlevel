f=int(input())
g=list(map(int,input().split()))
d=[]
h=[]
for i in g:
    if(i%2==0):
        continue
    else:
        d.append(i)
        break
for i in g:
    if(i%2!=0):
        continue
    else:
        d.append(i)
        break
print(d[1])
