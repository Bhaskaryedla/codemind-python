y=int(input())
z=int(input())
sum1=0
sum2=0
for i in range(1,y):
    if y%i==0:
        sum1+=i
for j in range(1,z):
    if z%j==0:
        sum2+=j
if(sum1==z and sum2==y):
    print("Amicable")
else:
    print("Not Amicable")
        