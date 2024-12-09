#Bài 12: Viết lệnh xóa thông tin của sinh viên trong danh sách sinh viên ở bài 10 ứng với tên được nhập vào bàn phím
ten_xoa = input("Nhap ten sinh vien can xoa: ")
xoa_thanh_cong = False
for sinh_vien in ds_sinh_vien:
    if ten_xoa in sinh_vien:
        ds_sinh_vien.remove(sinh_vien)
        xoa_thanh_cong = True
        break
if xoa_thanh_cong:
    print(f"Da xoa thong tin sinh vien co ten: {ten_xoa}")
else:
    print(f"Khong tim thay sinh vien co ten: {ten_xoa}")
print("\nDanh sach sinh vien sau khi xoa:")
print("Ten\tDiem")
for sinh_vien in ds_sinh_vien:
    for ten, diem in sinh_vien.items():
        print(f"{ten}\t{diem}")
