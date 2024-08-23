import datetime
import calendar

def get_weekdays(year, month, weekday):
    # Tạo một danh sách các ngày trong tháng
    days_in_month = calendar.monthrange(year, month)[1]
    dates = [datetime.date(year, month, day) for day in range(1, days_in_month + 1)]
    
    # Lọc ra các ngày là thứ mà người dùng yêu cầu
    weekdays = [date for date in dates if date.weekday() == weekday]
    return weekdays

def main():
    # Nhập năm và tháng từ người dùng
    year = int(input("Nhập năm: "))
    month = int(input("Nhập tháng: "))
    
    # Nhập thứ trong tuần từ người dùng (0: Thứ 2, 1: Thứ 3, ..., 6: Chủ nhật)
    days = ["Thứ 2","Thứ 3","Thứ 4","Thứ 5","Thứ 6","Thứ 7","Chủ Nhật"]
    for i in range(7):
        print("{}. {}".format(i,days[i]))
    weekday = int(input("Nhập thứ trong tuần (0: Thứ 2, 1: Thứ 3, ..., 6: Chủ nhật): "))
    
    # Lấy các ngày là thứ mà người dùng yêu cầu
    weekdays = get_weekdays(year, month, weekday)
    
    # In ra các ngày đó theo định dạng ngày/tháng/năm
    print(f"Các ngày là thứ {calendar.day_name[weekday]} trong tháng {month}/{year}:")
    for date in weekdays:
        print(date.strftime("%d/%m/%Y"))

if __name__ == "__main__":
    main()
