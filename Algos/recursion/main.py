def decend(n):
    print(n)
    if n > 1:
        decend(n - 1)

# decend(10)

def factorial(n):
    if n == 1:
        return n
    
    return n * factorial(n - 1)

print(factorial(3))

# O(2 ^ N)
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)

# print(fib(3))
# print(fib(7))
# 1, 1, 2, 3, 5, 8, 13 ....