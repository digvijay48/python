def powerofn(n):
    if n == 0:
        return 1
    else:
        power = powerofn(n-1)
        return power *2
print("Power of n",powerofn(4))