def is_prime(a):
    if a < 2:
        return False
    elif a!=2 and a % 2 == 0:
        return False
    else:
        return all (a % i for i in range(3, int(a**0.5)+1))
n = int(input("Nhập n: "))
aResult = "A = "
bResult = "B = "
cResult = "C = "
dResult = "D = "
a = 0
b = 0
c = 1
d = 0
for x in range(1, n+1):
    # A = tổng các số lẻ nhỏ hơn hay bằng n
    if(x % 2 != 0):
        a += x
        aResult += str(x) + " + "

    # B = tổng các số chẵn nhỏ hơn hay bằng n
    else:
        b += x
        bResult += str(x) + " + "

    # C = tích các số chia hết cho 3 nhỏ hơn hay bằng n
    if (x % 3 == 0):
        c *= x
        cResult += str(x) + " * "

    # D = tổng các số nguyên tố nhỏ hơn hay bằng n
    if is_prime(x):
        d += x
        dResult += str(x) + " + "


print(f'{aResult} = {a}')
print(f'{bResult} = {b}')
print(f'{cResult} = {c}')
print(f'{dResult} = {d}')
