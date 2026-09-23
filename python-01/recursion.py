# Recursion - A function calling itself
# Factorial, Fibonacci series, Stairs 

def fact(n):
    # Edge case handling
    if n == 0:
        return 1
    return n * fact(n - 1)
     

n = int(input())
print(fact(n))
# n = 5
# 5! = 5 x 4 x 3 x 2 x 1
# 5 x 4! => n x (n-1)!
# 4 x 3!
# 3 x 2!
# 2 x 1!
# 1 x 0!