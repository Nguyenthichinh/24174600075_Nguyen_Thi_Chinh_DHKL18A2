#bài 1 Viết chương trình nhập vào chuỗi ký tự, trả về số các từ trong chuỗi ký tự vừa nhập
chuoi_nhap = input("Nhap vao chuoi ky tu: ")
chuoi_nhap = chuoi_nhap.strip()  
tu=chuoi_nhap.split()
so_tu = len(tu)  
print("So tu trong chuoi la:", so_tu)
# Bài 2: Viết chương trình nhập vào chuỗi ký tự, trả về chuỗi ký tự sau khi loại bỏ tất cả các dấu cách thừa
chuoi_nhap_vao = input("nhap vao chuoi ky tu:")
tach_chuoi=chuoi_nhap_vao.split() 
chuoi_ket_qua = " ".join(tach_chuoi) 
print(f"chuoi ket qua: {chuoi_ket_qua}")
#bài 3 Viết chương trình nhập vào họ tên đầy đủ, trả về tên và họ riêng
ho_va_ten = input("nhap vao ten:")
ten_nhap_vao = ho_va_ten.split()
ho_ten=ten_nhap_vao[0] 
ten_dem=" ".join(ten_nhap_vao[1:]) 
print(f"ho: {ho_ten}")
print(f"ten dem: {ten_dem}")
#bài 4  Viết chương trình nhập vào chuỗi ký tự, trả về kết quả đếm số ký tự là chữ, số ký tự là số và số ký tự là ký tự đặc biệt (Không là số, không là chữ) trong chuỗi)
chuoi_nhap = input("Nhap vao chuoi ky tu: ")
chu_so = 0
chu_cai = 0
ky_tu_dac_biet = 0
for chu in chuoi_nhap:
    if chu.isdigit():
        chu_so =chu_so + 1
    elif chu.isalpha():
        chu_cai =  chu_cai + 1
    else:
        ky_tu_dac_biet =ky_tu_dac_biet + 1
print(f"So ky tu la chu: {chu_cai}")
print(f"So ky tu la so: {chu_so}")
print(f"So ky tu dac biet: {ky_tu_dac_biet}")
#bài 5 Viết chương trình nhập vào chuỗi ký tự, đếm xem có bao nhiêu chữ cái viết hoa, bao nhiêu chữ cái viết thường
nhap_vao_chuoi = input("nhap vao chuoi ky tu")
viet_hoa=0
viet_thuong=0
for chu in chuoi_nhap:
    if chu.isupper():
       viet_hoa=viet_hoa+1
    elif chu.islower():
        viet_thuong=viet_thuong+1
print(f"chu cai in hoa: {viet_hoa}")  
print(f"chu cai in thuong: {viet_thuong}")   
#bài 6  Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải là số âm hay không
nhap_vao_chuoi = input("nhap vao ky tu:")
if nhap_vao_chuoi.startswith('-') and chuoi_nhap[1:].isdigit(): 
    print(" chuoi la so am")
else:
    print(" chuoi khong phai so am")
#bài 7  Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải số thập phân hay không
nhap_vao_chuoi = input("nhap vao ky tu:")
if nhap_vao_chuoi.isdecimal() and  nhap_vao_chuoi.isdigit():    
             print(nhap_vao_chuoi.isdecimal())
             print("chuoi la so thap phan") 
else:
         print(" chuoi la so thap phan")                               
#bài 8  Viết chương trình nhập vào 2 xâu ký tự str_1 và str_2. Kiểm tra xem str_2 có nằm trong str_1 hay không và ngược lại
str_1 = input("Nhap vao chuoi str_1: ")
str_2 = input("Nhap vao chuoi str_2: ")
found_in_str_1 = False
for i in range(len(str_1) - len(str_2) + 1):  
    if str_1[i:i + len(str_2)] == str_2:
        found_in_str_1 = True
        break
if found_in_str_1:
    print(f"'{str_2}' nam trong '{str_1}'")
else:
    print(f"'{str_2}' khong nam trong '{str_1}'")
found_in_str_2 = False
for i in range(len(str_2) - len(str_1) + 1):  
    if str_2[i:i + len(str_1)] == str_1:
        found_in_str_2 = True  
        break
if found_in_str_2:
    print(f"'{str_1}' nam trong '{str_2}'")
else:
    print(f"'{str_1}' khong nam trong '{str_2}'")
# Bài 9: Viết chương trình nhập vào một chuỗi ký tự nhị phân 0 và 1. Kiểm tra xem chuỗi có phải số nhị phân không và chuyển đổi sang số thập phân
chuoi_nhi_phan = input("Nhập vào chuỗi nhị phân (chỉ gồm 0 và 1): ")
is_nhi_phan = True
for ky_tu in chuoi_nhi_phan:
    if ky_tu != '0' and ky_tu != '1':  
        is_nhi_phan = False
        break  
if is_nhi_phan:
    so_thap_phan = 0
    do_dai = len(chuoi_nhi_phan)
    for i in range(do_dai):
        bit = int(chuoi_nhi_phan[i])  
        so_thap_phan += bit * (2 ** (do_dai - i - 1))  
    print(f"Số thập phân tương ứng là: {so_thap_phan}")
else:
    print("Chuỗi không phải là số nhị phân hợp lệ.")

#bài 10
chuoi_nhap = input("Nhap vao chuoi ky tu: ")
so = ""  
chu = ""  

for ky_tu in chuoi_nhap:
    if ky_tu.isdigit():  
        so = so+ ky_tu
    else:  
        chu = chu +ky_tu

chuoi_moi = so + chu  
print("Chuoi moi sau khi don tat ca so