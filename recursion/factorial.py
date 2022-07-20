import sys
sys.setrecursionlimit(10000) #To increase the stack memory

def factorial(num):
    assert num >= 0 and int(num) == num, 'The number must be positive integer only'
    if num in [0,1]:
        return 1
    else:
        return num * factorial(num-1) #Recursive case
num=10.5
print("num ",int(num))
factorial=factorial(num)
print("factorial ",factorial)