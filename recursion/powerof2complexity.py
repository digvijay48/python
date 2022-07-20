def f(n):
    if n==1:
        return 1
    return f(n-1)+f(n-1)

print("F:",f(4))