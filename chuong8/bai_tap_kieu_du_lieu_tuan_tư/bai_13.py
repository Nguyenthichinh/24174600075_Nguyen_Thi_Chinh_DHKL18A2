#Bài 13: Viết lệnh thêm một sinh viên vào danh sách sinh viên ở bài 10. Với điều kiện:
# - Nếu tên sinh viên đã tồn tại, thông báo: "Thông tin sinh viên đã tồn tại"
# - Nếu chưa có sinh viên này, thông báo: "Đã thêm sinh viên"
ten_them = input("Nhap ten sinh vien can them: ")
diem_them = float(input("Nhap diem sinh vien can them: "))
sinh_vien_ton_tai = False
for sinh_vien in ds_sinh_vien:
    if ten_them in sinh_vien:
        sinh_vien_ton_tai = True
        break
if sinh_vien_ton_tai:
    print("Thong tin sinh vien da ton tai")
else:
    thong_tin_sinh_vien_moi = {ten_them: diem_them}
    ds_sinh_vien.append(thong_tin_sinh_vien_moi)
    print("Da them sinh vien")
print("\nDanh sach sinh vien sau khi them:")
print("Ten\tDiem")
for sinh_vien in ds_sinh_vien:
    for ten, diem in sinh_vien.items():
        print(f"{ten}\t{diem}")
