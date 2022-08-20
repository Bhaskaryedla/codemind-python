n=int(input())
m=int(input())
x=0
y=0
for i in range(1,n):
    if n%i==0:
        x=x+i
for j in range(1,m):
    if m%j==0:
        y=y+j
if (x==m and y==n):
    print("Amicable")
else:
    print("Not Amicable")