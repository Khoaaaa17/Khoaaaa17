n = int(input())
import math
def a():
    s = 0
    for _ in range(1,n+1):
        s += _ 
        _ = math.factorial(n)
    print(f'Tổng số n: {s} \n Tích (giai thừa) của 1 -> n: {_}')
def b():
    count=0
    for i in range(0,n):
        count=count+1
        i -= 1
    print("The number of digits in the number are:",count)
    for i in range(0,n+1):
        if i % 2 == 0:
            print(f'So chan: {i}',end = ' ')
        else:
            print(f'So le: {i}', end = ' ')
    

a()
b()

        
