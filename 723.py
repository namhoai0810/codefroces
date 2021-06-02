point = list(map(int, input().split()))

point.sort()
# print(point[2])
# print(point[1])
# print(point[0])
min_step = (point[2] - point[1]) + (point[1] - point[0])
print(min_step)