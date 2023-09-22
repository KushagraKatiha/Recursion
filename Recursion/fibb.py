def fibb(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fibb(x-2)+fibb(x-1)
            
    
x = 10
for i in range(x):
    print(fibb(i))

