def Fibonacci(n):
    if n == 0:
        return 0
    else:
        print(f'Fibonacci({n}):{n -1 + n - 2}')
        return Fibonacci(n-1) + Fibonacci(n-2)
for i in range (6):
    print("Fibonacci({i}): {r}".format(i=i,r=Fibonacci(i+1)))

        
Fibonacci(5)