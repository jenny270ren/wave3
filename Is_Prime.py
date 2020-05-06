def f1(n):
    
    if n>1:
        for a in range(n-2):
            if n%(a+2)==0:
                return False
    else:
        return False
    return True
b = int(input())
print(f1(b))