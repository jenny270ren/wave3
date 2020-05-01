n = int(input("enter an integer greater than 1: "))
f = 2
if n<2:
    print ("error")
else:
    print("the prime factors of",n,":")
    while f<=n:
        if n%f==0:
            print (f)
            n = n/f
        else:
            f+=1


