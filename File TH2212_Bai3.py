def so_lon_nhat(a,b,c):
    max = a
    if b > max:
       max = b
    if c > max:
       max = c
    return max

max = so_lon_nhat(4831,8451,211)
print(f"Số lớn nhất là: {max}")