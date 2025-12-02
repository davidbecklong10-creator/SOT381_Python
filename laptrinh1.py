#Tính BMI
chieu_cao = float(input("Nhập chiều cao của bạn (cm): "))
can_nang = float(input("Nhập cân nặng của bạn (Kg): "))

#Tính BMI
bmi = can_nang / (chieu_cao)**2

if bmi < 18.5:
    print("gầy")
elif 18.5 <= bmi < 25:
    print("Bình thường")
elif 25 <= bmi < 30:
    print("thừa cân")
else:
    print("Béo phì")