#Bài 3: Nhập vào số nguyên dương n.
#In ra màn hình: 
# - Danh sách A gồm các số lẻ nhỏ hơn n
# - Danh sách B gồm các số chẵn nhỏ hơn n
#Sắp xếp dãy số theo thứ tự giảm dần
while True:
    try:
        n = int(input("Nhập vào số nguyên dương n: "))
        if n > 0:
            break 
        else:
            print("Số vừa nhập không phải là số nguyên dương. Vui lòng thử lại!")
    except ValueError:
        print("Vui lòng nhập một số nguyên!")
A = []
B = []
for i in range(n-1, -1, -1):
    if i % 2 != 0:
        A.append(i) 
    else:
        B.append(i)  
print(f"Danh sách A (số lẻ):{A}")
print(f"Danh sách B (số chẵn):{B}")
