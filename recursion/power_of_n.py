# f(x,n) = x * f(x,n-1)
def powerofn(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * powerofn(x,n-1)

print("Power of n",powerofn(5,3))