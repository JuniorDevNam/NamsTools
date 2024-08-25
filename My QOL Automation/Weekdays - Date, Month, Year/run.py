import calendar
import sys
from os.path import join
output = join(sys.path[0],'output.txt')
def get_days_for_weekdays(year, month, weekday1, weekday2):
    # Tạo một lịch tháng
    cal = calendar.Calendar()
    days = []
    days2 = ["T2", "T3", "T4", "T5", "T6", "T7", "CN"]
    
    # Duyệt qua các ngày trong tháng
    for day in cal.itermonthdays2(year, month):
        if day[0] != 0:  # Loại bỏ các ngày không thuộc tháng hiện tại
            if day[1] == weekday1 or day[1] == weekday2:
                days.append(f"{day[0]:02d}/{month:02d}/{year} ({days2[day[1]]})")
    
    return days

# Nhập năm và tháng từ người dùng
year = int(input("Nhập năm: "))
month = int(input("Nhập tháng: "))
   
# Nhập thứ trong tuần từ người dùng (0: Thứ 2, 1: Thứ 3, ..., 6: Chủ nhật)
days = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật"]

for i in range(7):
    print("{}. {}".format(i+2, days[i]))
day = int(input("Nhập thứ trong tuần (2: Thứ 2, 3: Thứ 3, ..., 8: Chủ nhật): "))
them = input("Xác nhận thứ? (0: OK, 1: Thêm thứ): ")
if them == "1":
    day2 = int(input("Nhập thứ trong tuần (2: Thứ 2, 3: Thứ 3, ..., 8: Chủ nhật): "))
    weekday2 = day2-2
else:
    weekday2 = -1
weekday1 = day-2

weekdays = get_days_for_weekdays(year, month, weekday1, weekday2)
print(f"Các ngày trong tháng {month}/{year} là thứ {days[weekday1]} hoặc thứ {days[weekday2]}: ")
# Mở tệp ở chế độ ghi để xóa nội dung
with open(output, 'w') as file:
    pass
with open(output, 'a', encoding="utf-8") as o:
    for x in weekdays:
        o.write(x + "\n")
    o.write(f"Tổng 0{len(weekdays)} buổi\n")
