can = ['Canh', 'Tân', 'Nhâm,', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh','Mậu','Kỷ']
chi = ['Thân', 'Dậu', 'Tuất', 'Hợi','Tí','Sửu','Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', "Mùi"]
namDL = int(input("Nhập năm dương lịch: "))

can1 = namDL % 10
chi1 = namDL % 12
namAL = can[can1] + " " + chi[chi1]
print(namAL)