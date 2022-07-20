def findbiggestelement(n):
    if n==1:
        return ar[0]
    return max(ar[n-1],findbiggestelement(n-1))
ar=[2,4,56,6,8,1,10,11,50,34,25]
print("findbiggestelement:",findbiggestelement(len(ar)))