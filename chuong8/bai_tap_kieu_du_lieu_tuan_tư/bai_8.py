#Bài 8: Viết chương trình đảo vị trí hai cột i, j của ma trận A kích cỡ m*n
m = int(input("Nhập số hàng (m): "))
n = int(input("Nhập số cột (n): "))
A = []
print("Nhập các phần tử của ma trận:")
for i in range(m):
    hang = list(map(int, input(f"Nhập hàng {i+1}: ").split()))
    A.append(hang)
i = int(input(f"Nhập chỉ số cột thứ nhất (từ 0 đến {n-1}): "))
j = int(input(f"Nhập chỉ số cột thứ hai (từ 0 đến {n-1}): "))
print("\nMa trận trước khi đảo:")
for hang in A:
    print(hang)
for hang in A:
    hang[i], hang[j] = hang[j], hang[i]
print("\nMa trận sau khi đảo:")
for hang in A:
    print(hang)
