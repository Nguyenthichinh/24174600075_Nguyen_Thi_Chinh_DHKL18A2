#Bài 14: Viết lệnh sửa thông tin của một sinh viên ở bài 10 ứng với tên được nhập vào bàn phím
ten_sua = input("Nhap ten sinh vien can sua: ")
sinh_vien_ton_tai = False
for sinh_vien in ds_sinh_vien:
    if ten_sua in sinh_vien:
        sinh_vien_ton_tai = True
        diem_moi = float(input(f"Nhap diem moi cho sinh vien {ten_sua}: "))
        sinh_vien[ten_sua] = diem_moi
        print(f"Da sua thong tin sinh vien {ten_sua}.")
        break
if not sinh_vien_ton_tai:
    print(f"Khong tim thay sinh vien co ten: {ten_sua}")
print("\nDanh sach sinh vien sau khi sua:")
print("Ten\tDiem")
for sinh_vien in ds_sinh_vien:
    for ten, diem in sinh_vien.items():
        print(f"{ten}\t{diem}")