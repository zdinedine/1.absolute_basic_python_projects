def serazeni(x):
    z=[]
    g=[]
    l = 0
    while l<1000000:
     for y in x:
        if y == l:
         z.append(y)
        else: g.append(y)
     l += 1

    print(z)

serazeni([3,1,6,8,2,5])