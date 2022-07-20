# f(n) = n%10 + f(n/10)
def sumofdigits(n):
    if n<=0 :
        return 0
    else :
        return n%10+sumofdigits(n//10)

print("Sum of digits:",sumofdigits(12345))