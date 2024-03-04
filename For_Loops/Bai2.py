# Viết CT có các hàm sau:
# a) Check 1 Số tự nhiên có phải số nguyên tố ?
# b) In ra các số NT <= n. Sử dụng hàm câu a
# c) Hàm tìm số NT nhỏ nhất > n

def LaSNT(n):
    if n < 2: return False
    for i in range(2, n//2 +1):
        if n % i == 0: return False
    # Nếu không phải 2 trường hợp trên => n là SNT
    return True

def InSNT(n):
    for i in range(2, n+1):
        if LaSNT(i):
            print(i, end=" ")

def TimSNT(n):
    i = n + 1
    while True:
        if LaSNT(i):
            print("Số nguyên tố nhỏ nhất lớn hơn {} là: {}".format(n, i))
            break
        i += 1

# main
if __name__ == '__main__':
    n = 100
    # print(LaSNT(n))
    InSNT(n)
    print("Các số nguyên tố <= {}:".format(n))
    TimSNT(n)