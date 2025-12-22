a = int(input("Nhập số: "))
b = int(input("Nhập số: "))
c = int(input("Nhập số: "))

max = a
if b > max:
    max = b
if c > max:
    max = c

print(f"Số lớn nhất là: {max}")