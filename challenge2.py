import math

PHI = (1 + 5 ** 0.5) / 2
SQ5 = math.sqrt(5)
def fibonacci(n):

    return int(math.floor(math.log(n*SQ5 + 0.5,PHI)) - 1)

def exponential_series(n):
    height = math.log(n + 1,2)
    return int(height)

def answer(total_lambs):
    return fibonacci(total_lambs) - exponential_series(total_lambs)

# for n in range(1, 99):
#     print(n, fibonacci(n), exponential_series(n), answer(n))
