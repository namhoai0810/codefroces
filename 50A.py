width, size_long = map(int, input().split())
if (width == 1 and size_long == 1):
    print(0)
else:
    print((width * size_long) // 2)