def chuyendoigio():
    seconds = int(input('Nhap so giay: '))
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print(f'{h:02d}:{m:02d}:{s:02d}') 
chuyendoigio()
def DTB_va_Xep_loai():
    mieng = float(input('Nhập điểm miệng: '))
    diem15p = float(input('Nhập điểm 15p: '))
    diem1tiet = float(input('Nhập điểm thi 1 tiết: '))
    thi= float(input('Nhập điểm thi: '))
    dtb = (mieng+diem15p+diem1tiet*2+thi*3)/7
    print(dtb)
    if dtb >= 8:
        print('G')
    elif dtb >= 6.5:
        print('K')
    elif dtb >= 5:
        print('TB')
    elif dtb >= 3.5:
        print('Y')
    else:
        print('Kém')
DTB_va_Xep_loai()
















    