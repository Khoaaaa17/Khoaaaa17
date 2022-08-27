def hinhvuongbangkytu():
    n = input('Nhập ký tự muốn xuất hiện: ')
    i = int(input("Nhập cạnh hình vuông: "))
    for _ in range(i):
        print(i*n)
def hinhvuongrongcach1():
    h = int(input())
    for k in range(h):
        for o in range(h):
            if o == 0 or o == h-1  or k == 0 or k == h-1:
                print('*',end = "")
            else:
                print(" ",end = "")
        print(" ")
def hinhvuongrongcach2():
    doc = int(input('Nhập hàng dọc: '))
    ngang = int(input('Nhập hàng ngang: '))
    for i in range(doc):
        for j in range(ngang):
            if i == 0 or i == doc-1 or j == 0 or j == ngang-1:
                print('*',end =" ")
            else:
                print(" ",end= " ")
        print()
def vuongrong():
    n = input('Nhập ký tự: ')
    i = int(input('Nhập độ dài hình vuông: '))
    for k in range(i):
        for h in range(i):
            if h == 0 or h == i-1 or k == 0 or k == i-1:
                print(n,end =" ")
            else:
                print(" ",end=" ")
        print()

vuongrong()
