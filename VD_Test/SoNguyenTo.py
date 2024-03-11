# Bài tập: Nhập 1 số nguyên n thỏa 0 < n <= 1000 (Lặp lại việc nhập cho đến khi n thỏa ràng buộc)
#          a) Kiểm tra n có phải là số nguyên tố ?
#          b) In ra các SNT <= n.

#   B1. Input (Có ràng buộc tương tự lệnh do ... while)
while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0 and n <=1000:
        break
#   B2. 
#   Định nghĩa hàm kiểm tra 1 số tự nhiên có phải SNT
def LaSNT(n):
    if n < 2:
        return False
    for i in range(2, n//2 + 1):
        if n % i ==0:
            return False
        return True
#   a. 
if  LaSNT(n):
    print("{} là số nguyên tố".format(n))
else:
    print("{} không phải là số nguyên tố".format(n))
#   b.
print("Các số nguyên tố <= {}:".format(n))
for i in range(2, n+1):
    if LaSNT(i):
        print("%5d" % i, end=" ")
