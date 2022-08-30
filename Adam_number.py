n=int(input())
rev=0
a=n**2
num=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
b=rev**2
q=b
x=0
while b>0:
    r=b%10
    x=x*10+r
    b=b//10
if(x==a):
    print("True")
else:
    print("False")
    