import sys
sys.setrecursionlimit(10000)
def fibonacci(n):
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print("fibonacci ",fibonacci(100))