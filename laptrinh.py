mon_1 = float(input("Nhập điểm môn Toán: "))
mon_2 = float(input("Nhập điểm môn Lý: "))
mon_3 = float(input("Nhập điểm môn Hóa: "))

tong_diem = mon_1 + mon_2 + mon_3
if tong_diem >= 15:
    if mon_1 >= 4 and mon_2 >= 4 and mon_3 >= 4:
        print("Đậu")
        if mon_1 > 5 and mon_2 > 5 and mon_3 > 5:
            print("Học đều các môn")
        else:
            print("Học chưa đều các môn")
else:
    print("Thi hỏng5")