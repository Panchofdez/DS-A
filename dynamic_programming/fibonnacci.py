#using dynamic programming to find any number in a fibonacci sequence
def fib1(n):
    #using tabulation method
    table = [-1] * (n + 1)
    table[0] = 0
    table[1] = 1

    for i in range(2, n+1):
        table[i] = table[i -1] + table[i-2]


    return table[n]

n =5
#our table to store values
table = [-1] * (n+1)
def fib2(n):
    #using recursion and memoization
    if n < 2:
        return n
    if table[n] != -1:
        return table[n]
    else:
        return fib2(n-1) + fib2(n-2)

print(fib2(n))