n=int(input())
x=0
prod=1
while n>0:
    s=n%10
    x=x+s
    prod=prod*s
    n=n//10
if(x==prod):
    print("Spy Number")
else:
    print("Not Spy Number")