def a():
    x = float(input())
    y = float(input())
    if pow(x,2) + pow(y,2) <= 1:
        print(f'z = {pow(x,2) + pow(y,2)}')
    elif pow(x,2) + pow(y,2) > 1 and y >= x:
        print(f'z = {x+y}')
    else:
        print(f'z = {0.5}')
def b():
    x = float(input())
    y = float(input())
    a = float(input())
    b = float(input())
    r = float(input())  
    if pow((x-a),2) + pow((y-b),2) == pow(r,2):
        print(f'z = {abs(x) + abs(y)}')
    else:
        print(f'z = {x+y}')
a()
b()
