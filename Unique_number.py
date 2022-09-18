m=int(input())
n=str(m)
o=list(n)
p=set(o)
p=list(p)
if len(p)==len(o):
    print("Unique Number")
else:
    print("Not Unique Number")
