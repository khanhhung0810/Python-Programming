a = [1,2,3,4]
b = []
for i in range(len(a)):
    b.append(a[i]**2)
    print(b)
# Cách 2: dùng hàm map
def Square(x):
    return x**2
b = map(Square, a)
b = list(b)
print(b)