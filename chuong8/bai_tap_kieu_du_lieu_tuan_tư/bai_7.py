#Bài 7: Viết chương trình đảo vị trí hai hàng i, j của ma trận A kích cỡ m*n
#1 0 0 0
#0 1 0 0
#0 0 1 0
#0 0 0 1
i = int(input("Nhap vao hang i: "))
j = int(input("Nhap vao hang J: "))
[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
temp = ma_tran_don_vi[i]
ma_tran_don_vi[i] = ma_tran_don_vi[j]
ma_tran_don_vi[j] = temp
print(ma_tran_don_vi)