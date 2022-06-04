n=int(input())
a=0
b=1
if(n==0 and n==1):
    print('True')
while (True):
    c=a+b
    a=b
    b=c
    if c==n:
        print('True')
        break
    elif c>n:
        print('False')
        break