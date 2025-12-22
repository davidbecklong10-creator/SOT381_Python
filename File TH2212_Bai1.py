while True:
    w = float(input("Nhập chiều dài: "))
    r = float(input("Nhập chiều rộng: "))
    if w >= 0.0 and r <= 100.0:
        chu_vi = 2 * ( w + r )
        dien_tich = w * r
        print(f"Chu vi hình chữ nhật là: {chu_vi:.2f}")
        print(f"Diện tích hình chữ nhật là: {dien_tich:.2f}")
        break
    else:
        print("Vui lòng nhập lại")
    
