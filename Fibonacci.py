num=int(input("Num = "))
def Fibonacci(c,a=0,b=1):
    if c!=0:
        print(f"{a}",end=" ")
        c-=1
        Fibonacci(c,b,a+b)
Fibonacci(num+2)