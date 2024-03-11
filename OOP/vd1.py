#   Viết chương trình OOP Python giải quyết bài toán sau:
#   Nhập 1 danh sách n điểm trong mặt phẳng. Mỗi điểm có tọa độ (x,y)
#       a. In ra danh sách điểm và tọa độ.
#       b. Tìm điểm ở xa gốc tọa độ nhất.
#       c. Tìm cặp điểm gần nhau nhất.
import math

class Point:
    def __init__(self, x=0, y=0) :
        self.x=y
        self.y=y
    
    def distance(self, p):
        return math.sqrt((self.x-p.x)**2 + (self.y-p.y)**2)
    
    def print_info(self):
        print("({} , {})".format(self.x, self.y))


n = int(input("Nhập số điểm trong mặt phẳng: "))
point_list = []

for i in range(n):
    print("Nhập điểm thứ {}:".format(i+1))
    x = int(input("x = "))
    y = int(input("y = "))
    p = Point(x,y)
    point_list.append(p)

for p in point_list:
    p.print_info()
goc_toa_do = Point(0,0)
max_distance = point_list[0].distance()
max_point = point_list[0]

for p in point_list[1:]:
    dist = p.distance(goc_toa_do)
    if dist > max_distance:
        max_distance = dist
        max_point = p

print("Điểm xa nhất: ")
max_point.print_info()
#   Tìm cặp điểm gần nhau nhất
closest_point1, closest_point2 = point_list[0], point_list[1]
min_distance = closest_point1.distance(closest_point2)
for i in point_list [:-1]:
    for p2 in point_list:
        if p1 != p2:
            if p1.distance(p2) < min_distance:
                min_distance = p1.distance(p2)
                closest_point1, closest_point2 = p1, p2
print("Cặp điểm gần nhau nhất là: ")
closest_point1.print_info()
closest_point2.print_info()
print("Khoảng cách = %.2f" % (min_distance))