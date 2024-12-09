#Bài 11: Viết lệnh in danh sách sinh viên ở bài 10. Có dạng:
#Ten    Diem
#Dung   10.0
#Quang  5.3
#Trang  7.5
# In danh sách sinh viên
print("Ten\tDiem")
for sinh_vien in ds_sinh_vien:
    for ten, diem in sinh_vien.items():
        print(f"{ten}\t{diem}")