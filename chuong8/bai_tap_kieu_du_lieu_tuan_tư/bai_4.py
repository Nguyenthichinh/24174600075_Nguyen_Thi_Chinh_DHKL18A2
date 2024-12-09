#Bài 4: Viết chương trình sinh ra ma trận K kích cỡ m*n chỉ chứa số 0
#Bài làm
m = int(input("Nhap vao so cot cua ma tran m = "))
n = int(input("Nhap vao so hang cua ma tran n = "))
#0 ... m
#.     .
#.     .
#.     .
#n ... 0
ma_tran_a = [[0,0,0],
             [0,0,0],
             [0,0,0]]
ma_tran_a = []
for hang in range(n):
    phan_tu_trong_hang = []
    for cot in range(m):
        phan_tu_trong_hang.append(0)
    ma_tran_a.append(phan_tu_trong_hang)
print(ma_tran_a)

ma_tran_a = [[0]*m]*n 
print(ma_tran_a)