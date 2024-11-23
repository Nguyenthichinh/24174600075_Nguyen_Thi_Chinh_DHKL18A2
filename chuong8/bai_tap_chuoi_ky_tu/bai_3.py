#bài 3 Viết chương trình nhập vào họ tên đầy đủ, trả về tên và họ riêng
ho_va_ten = input("nhap vao ten:")
ten_nhap_vao = ho_va_ten.split()
ho_ten=ten_nhap_vao[0] 
ten_dem=" ".join(ten_nhap_vao[1:]) 
print(f"ho: {ho_ten}")
print(f"ten dem: {ten_dem}")