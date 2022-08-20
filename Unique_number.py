n=int(input())
m=str(n)
x=list(m)
y=set(x)
y=list(y)
if len(y)==len(x):
    print("Unique Number")
else:
    print("Not Unique Number")