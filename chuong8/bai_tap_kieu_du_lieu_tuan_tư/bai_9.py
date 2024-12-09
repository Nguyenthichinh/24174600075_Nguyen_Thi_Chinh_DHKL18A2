#Bài 9: Viết chương trình nhập vào hai ma trận A, B có cùng kích thước.
#Tính:
# - Tổng hai ma trận A, B
# - Hiệu hai ma trận A, B
# - Tích của ma trận A với số k nhập từ bàn phím
# - Tích hai ma trận A, B
# - Ma trận đối xứng của ma trận A
n = int(input("Nhập kích thước ma trận (n x n): "))
print("Nhập ma trận A:")
A = []
for i in range(n):
    hang = list(map(int, input(f"Hàng {i + 1}: ").split()))
    A.append(hang)
print("Nhập ma trận B:")
B = []
for i in range(n):
    hang = list(map(int, input(f"Hàng {i + 1}: ").split()))
    B.append(hang)
tong = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(A[i][j] + B[i][j])
    tong.append(hang)
hieu = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(A[i][j] - B[i][j])
    hieu.append(hang)
k = int(input("Nhập số k để nhân với ma trận A: "))
tich_k_A = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(A[i][j] * k)
    tich_k_A.append(hang)
tich_A_B = []
for i in range(n):
    hang = []
    for j in range(n):
        tong = 0
        for k in range(n):
            tong += A[i][k] * B[k][j]
        hang.append(tong)
    tich_A_B.append(hang)
doi_xung_A = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(A[j][i])
    doi_xung_A.append(hang)
print("\nTổng hai ma trận A và B:")
for hang in tong:
    print(hang)
print("\nHiệu hai ma trận A và B:")
for hang in hieu:
    print(hang)
print(f"\nTích của ma trận A với số k ({k}):")
for hang in tich_k_A:
    print(hang)
print("\nTích hai ma trận A và B:")
for hang in tich_A_B:
    print(hang)
print("\nMa trận đối xứng của ma trận A:")
for hang in doi_xung_A:
    print(hang)

