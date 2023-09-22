def waysOf(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        result = waysOf(x-1) + waysOf(x-2)
        return result
    
x = 10

result = waysOf(x)
print(result)