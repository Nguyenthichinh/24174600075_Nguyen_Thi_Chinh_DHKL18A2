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