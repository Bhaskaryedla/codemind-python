a,b=map(int,input().split())
for m in range(1,b+1):
    if(a*m)%b==0:
        print(a*m)
        break