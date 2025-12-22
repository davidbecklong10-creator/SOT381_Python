def so_lon_nhat_vasoNN(a,b,c):
    LN = a
    NN = a
    if b > LN:
       LN = b
    if c > LN:
       LN = c
    if b < NN:
        NN = b
    if c < NN:
        NN = c
    return LN, NN

LN, NN = so_lon_nhat_vasoNN(43213,63156,131)
print(f"Số lớn nhất là: {LN}")
print(f"Số nhỏ nhất là: {NN}")
