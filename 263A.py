tmp_i = 0
tmp_j = 0
for i in range(1,6):
    matrix = [int(x) for x in input().split()]
    for j in range(1,6):
        if(matrix[j-1] != 0):
            tmp_i = i - 1
            tmp_j = j - 1
# print(tmp_i)
# print(tmp_j)
print(abs(2 - tmp_i) + abs(2 - tmp_j))            