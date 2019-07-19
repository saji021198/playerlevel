f,g=map(str,input().split())
c=0
for i in f:
    for j in g:
        if i==j:
            c=1
            break
if(c==1):
    print("yes")
else:
    print("no")
