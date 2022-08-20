n=int(input())
m=n*n
s=str(n)
x=str(m)
if x.endswith(s):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")