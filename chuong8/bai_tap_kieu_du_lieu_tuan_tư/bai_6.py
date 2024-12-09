#Bài 6: Viết chương trình nhập vào ma trận A kích cỡ m*n và in ra màn hình
m = int(input("Nhập số hàng (m): "))
n = int(input("Nhập số cột (n): "))
print(f"Nhập các phần tử của ma trận {m}x{n}, mỗi phần tử cách nhau bởi dấu cách:")
A = []
for i in range(m):
    while True:
        try:
            hang = list(map(float, input(f"Nhập hàng {i + 1}: ").split()))
            if len(hang) == n:
                A.append(hang)
                break
            else:
                print(f"Vui lòng nhập đúng {n} phần tử!")
        except ValueError:
            print("Vui lòng nhập các số hợp lệ!")
print("Ma trận A là:")
for hang in A:
    print(" ".join(map(str, hang)))