def fibonacci_iterativo(n):
    a = 0
    b = 1
    for i in range(0, n):
        print(a) 
        s = a + b 
        a, b = b,  s 

fibonacci_iterativo(5)