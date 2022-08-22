m=int(input())
while(True):
    if m%2==0:
        m//=2
    elif m%3==0:
        m//=3
    elif m%5==0:
        m//=5
    elif m==1:
        print("Ugly Number")
        break
    else:
        print("Not Ugly Number")
        break
    
    
        