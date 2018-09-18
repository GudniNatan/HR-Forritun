# Your function definition goes here
def fibo(n):
    a = 0
    b = 1
    c = 1
    for i in range(n):
        print(b, end=" ")
        a = b
        b = c
        c = a + b


n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here        
fibo(n)