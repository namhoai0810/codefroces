n = int(input())
level_x = list(map(int, input().split()))
level_y = list(map(int, input().split()))

set_level = set(level_x[1:] + level_y[1:])

if(len(set_level) == n):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")