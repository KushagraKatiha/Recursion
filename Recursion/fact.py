def fact(x):
    if x==0 or x==1:
        return 1
    else: 
        result = x*fact(x-1)

    return result
    

print(fact(5))