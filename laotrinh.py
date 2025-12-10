#Tính lãi xuất
so_tien = int(input("Nhập số tiền bạn muốn đầu tư: "))
lai = 0.07
for nam in range(0,10):
    tien_nhan = so_tien + so_tien * lai * nam
    print(f"Năm thứ {nam} bạn nhân được {tien_nhan:,.0f}.")
