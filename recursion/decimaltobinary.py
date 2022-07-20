def decimaltobinary(n):
    if n==1:
        return str(1)
    else:
        return decimaltobinary(n//2)+str(n%2)

print("Decimal to binary:",decimaltobinary(11))