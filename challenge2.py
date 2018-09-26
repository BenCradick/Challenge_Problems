import math
def fibonacci(n):
    nodes = 0
    total = 0
    current = 1 
    previous = 0 
    penultimate = 0
    while(total + current <= n):
        total += current
        penultimate = previous
        previous = current
        current = penultimate + previous
        nodes += 1
    return nodes
def exponential_series(n):
    height = math.log(n + 1,2)
    height = math.floor(height)
    return height

def answer(total_lambs):
    return fibonacci(total_lambs) - exponential_series(total_lambs)
answer(20)