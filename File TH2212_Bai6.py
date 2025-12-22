n = int(input("Nhập số lượng bài hát: "))
dsBH = []
print("Thêm tên bài hát")
for i in range(n):
    tenBH = input("Nhập tên bài hát: ")
    dsBH.append(tenBH)
    
    
print("In hoa toàn bộ danh sách")
for i in range(n):
    ten = dsBH[i]
    print(ten.upper())

for i in range(n):
    ten = dsBH[i]
    if ten.find("yeu") == -1:
       print(f"Bài {i}: {ten}")
       
print("Bài dài nhất")
tenbaidainhat = dsBH[0]
sotucuabaidainhat = len(tenbaidainhat.split())
vitricuabai = 0

for i in range(n):
    tenbai=dsBH[i]
    sotu = len (tenbai.split())
    if sotu > sotucuabaidainhat:
        vitricuabai = i
        tenbaidainhat = tenbai
        sotucuabaidainhat = sotu
print(f"Bài: {tenbaidainhat} ở vị trí {vitricuabai} có {sotucuabaidainhat} từ")