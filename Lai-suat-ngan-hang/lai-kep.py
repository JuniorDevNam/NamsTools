t = int(input("Số tiền gốc ban đầu gửi vào: "))
l = float(input("% lãi suất/năm: "))
g = int(input("Số tháng gửi: "))

a = l / 12 / 100
c = t
for x in range(1,g+1):
    c = c + c*a
print(c)
