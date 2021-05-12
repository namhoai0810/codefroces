n = int(input())
soldiers = [int(x) for x in input().split()]



min_index = n - 1 - soldiers[::-1].index(min(soldiers))
max_index = soldiers.index(max(soldiers))

# print(soldiers[::-1])
# print(soldiers[::-1].index(min(soldiers)))
# print(min_index)
# print(max_index)
steps = max_index + (n - 1 - min_index)

print(steps if min_index > max_index else steps - 1)