import math

PHI = (1 + math.sqrt(5)) / 2
SQ5 = math.sqrt(5)



def fibonacci(n):
    if is_fib(n + 1):
        return math.floor(math.log(n*SQ5 + 1/PHI, PHI) - 1)
    else:
        return math.floor(math.log(n*SQ5 + 1/PHI, PHI) - 2)

def is_fib(n):
    k = float(5*n**2)
    j = (k - 4)
    l = (k + 4)
    j1 = math.floor(math.sqrt(j))**2
    l1 = math.floor(math.sqrt(l))**2
    if (j == j1) or (l == l1):
        return True
    else:
        return False


def exponential_series(n):
    height = math.log(n + 1,2)
    return int(height)

def answer(total_lambs):
    return fibonacci(total_lambs) - exponential_series(total_lambs)
