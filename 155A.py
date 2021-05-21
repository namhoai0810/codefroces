contest = int(input())
points = list(map(int, input().split()))

points_min = points[0]
points_max = points[0]
count = 0
for item in points:
    if(item > points_max):
        points_max = item
        count = count + 1
    if(item < points_min):
        points_min = item
        count = count + 1

print(count)