n=int(input())
rev=0
num=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if(rev==num):
    print("True")
else:
    print("False")