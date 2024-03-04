# Một máy ATM có các loại tiền 100, 200 và 5 USD. 
# Một người cần rút số tiền m.
# a) Tìm phương án rút tốt nhất (Có ít tờ tiền nhất)
# b) Liệt kê tất cả các cách rút được số tiền m. Có tất cả bnh cách ?
while True:
    m = int(input("Nhập số tiền rút: "))
    if m <= 0 or m %5 !=0:
        print("Số tiền không thỏa mãn.")
    else:
        break
#a)
m1 =m
soTo100 = m // 100 # Chia lấy phần nguyên
m = m % 100        # Số tiền còn lại
soTo20 = m //20
m = m % 20         # Số tiền còn lại
soTo5 = m // 5
# In Kết quả
print("Phương án rút tiền tốt nhất")
print("{} tờ 100 + {} tờ 20 + {} tờ 5.".format(soTo100,soTo20,soTo5))
print("======================================")
print("Tất cả các cách: ")

m = m1 
soCach =0 
for soTo100 in range(m//100+1):
    for soTo20 in range(m//20+1):
        for soTo5 in range(m//5+1):
            if soTo100*100 + soTo20*20 + soTo5*5==m:
                soCach += 1
                print("{}: {}tờ 100 + {} tờ 20 + {} tờ 5.".format(soCach,soTo100,soTo20,soTo5))
print("Có tất cả {} cách rút.".format(soCach))