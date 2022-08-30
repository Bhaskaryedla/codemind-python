n=int(input())
length=len(str(n))
temp=n
sum=0
while temp>0:
    r=temp%10
    sum=sum+int(r**length)
    temp=temp//10
    length=length-1
if(sum==n):
    print("True")
else:
    print("False")
