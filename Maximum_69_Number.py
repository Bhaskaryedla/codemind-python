m=int(input())
m=str(m)
m=list(m)
for i in range(len(m)):
    if m[i]=='6':
        m[i]='9'
        break
m=''.join(m)
print(m)
    