#Bài 10: Lập một danh sách với n sinh viên bao gồm thông tin tên và điểm tổng kết cuối năm của các sinh viên đó
# thong_tin_sinh_vien = {"Hung": 4.0}
# ds_sinh_vien = [{"Hung": 4.0},{"Hung": 4.0},{"Hung": 4.0},{"Hung": 4.0}]
ds_sinh_vien = []
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    thong_tin_sinh_vien = {ten: diem}
    ds_sinh_vien.append(thong_tin_sinh_vien)