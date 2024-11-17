#Bài tập vềchuôi kí tự
#dựng thứ nhất: áp dụng sử lí chuỗi kí tụ bằng các phương thức có sẵn
#Bài 1: Nhập môttj chuỗi kí tự bất kì. đếm số kí tự tong chuỗi.
#Cách một:
chuoi_nhap_vao = input("nhat vao chuoi bat ky: ")
so_ky_tu_trong_chuoi = len(chuoi_nhap_vao)
print(f"So ky tu trong chuoi la {so_ky_tu_trong_chuoi}")
#Cách 2:
chuoi_nhap_vao =  input("Nhap vao chuoi bat ky: ")
dem = 0
for chu in chuoi_nhap_vao:
    dem = dem + 1
print("So ky tu trong chuoi la {dem}")
    
#Bài 2: Nhập vào một chuỗi bất kỳ. xóa các khoảng trống ở đầu và cuối chuỗi 
#cách 1
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
chuoi_da_xoa_khoang_trong = chuoi_nhap_vao.strip()
print(f"Chuoi sau khi xoa khoang trong {chuoi_da_xoa_khoang_trong}")
#cách 2:
chuoi_nhap_vao = input("Nhap vao chuoi bat ki: ")
#"   chuoi nhao vao               "
chuoi_xu_ly_dau = ""
kiem_tra_dau = False
for chu in chuoi_nhap_vao:
    if chu == " " and kiem_tra_dau == false
        continue
    else:
        kiem_tra_dau == True
        chuoi_xu_ly_dau = chuoi_xu_ly_dau + chu
        
chuoi_dao_nguoc = chuoi_xu_ly_dau[::-1]
chuoi_dao_nguoc_xu_ly_dau        
kiem_tra_dau = False
for chu in chuoi_dao_nguoc:
    if chu == " " and kiem_tra_dau == false
        continue
    else:
        kiem_tra_dau == True
        chuoi_dao_nguoc_xu_ly_dau = chuoi_dao_nguoc_xu_ly_dau + chu

chuoi_ket_qua = chuoi_dao_nguoc_xu_ly_dau[::-1]
print(f"Chuoi sau khi xoa khoang trong {chuoi_ket_qua}")

#bài 3: Nhâph vào một chuỗi bất kỳ. Xóa tất cả các khoảng trống thừa trong chuỗi
#Ví dụ: "      chuoi   nhap    vao        "
#cách 1:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
tach_chuoi = chuoi_nhap_vao.split()
chuoi_ket_qua = " ".join(tach_chuoi)    
#"chuo nhap vao"
print(f"Chuoi ket qua: {chuoi_ket_qua}")

#Cách 2 bài tập ề nhà xử lý yêu cầu trên mà không sử dụng các phương thức    
        
    
    
#Dang thứ hai: áp dụng kết hợp xử lý vòng lặp và xử lý chuỗi kí tự
#Bài 1: Nhập vào môttj chuôi bất kỳ. Đếm xem có bao nhiêu ký tự là số à bao nhiêu ký tụe đặc biệt 
# isalpha(): kiểm tra chữ cái 
# isalpha(): kiểm tra số

chuoi_nhap_ao = input("Nhap vao chuoi bat ky: ")
dem_chu = 0
dem_so = 0
dem_ky_tu_dac_biet = 0
for chu in chuoi_nhap_vao:
    if chu.isalpha() == True
    dem_chu + 1
else:
    if chu.isdigit() == True
    dem_so = dem_so + 1
else:
    dem_ky_tu_dac_biet = dem_ky_tu_dac_biet + 1
    
print(f"So chu cai: { dem_chu}")
print(f"so so: {dem_so}")
print(f"So_ky_tu_dac_biet: {dem_ky_tu_dac_biet}")



