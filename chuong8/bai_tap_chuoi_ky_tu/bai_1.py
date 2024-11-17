# Bài 1: Viết chương trình nhập vào chuỗi ký tự, trả về số các từ trong chuỗi ký tự vừa nhập
chuoi = input("Nhập vào chuỗi ký tự: ")
danh_sach_tu = chuoi.split()
so_luong_tu = len(danh_sach_tu)
print("Số lượng từ trong chuỗi là:", so_luong_tu)
