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