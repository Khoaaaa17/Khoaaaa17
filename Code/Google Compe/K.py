s = 0
n = 1
while True:
    try:
        a,b = map(int,input().strip().split())
    except ValueError:
        print("Xin lỗi, không được nhập chữ")
        continue
    if a > b:
        print('Số a không được nhỏ hơn số b')
        continue
    elif a < 100 or b > 999:
        continue
        print("Xin lỗi, số bạn phải có 3 chữ số")
    else:
        break
for i in range(a,b+1):
    print(f'Các số trong phạm vi 2 số này là: {i}')
    if i % 2 == 0:
        s += i
    else:
        n *= i

print(f'Tổng số chẵn: {s}')
print(f'Tích số lẻ: {n}')
