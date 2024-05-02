t = int(input("Số tiền gốc ban đầu gửi vào: "))
l = float(input("% lãi suất/năm: "))
g = int(input("Số tháng gửi: "))

a = l / 12 / 100
c = t
for x in range(1,g+1):
    c = c + c*a
print(c)
#côg thức của phong:
print(t+(g/200)*((t-1/200**(g-1))/(t-1/200))+t/200**g)