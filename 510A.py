m,n = map(int, input().split())
for i in range(1, m+1):
    if(i % 4 == 0):
        print("")
        print('#',end='')
        for i in range(0, n -1):
            print('.', end='')
        print("")
    elif(i % 4 == 2):
        print("")
        for i in range(0, n -1):
            print('.', end='')
        print('#')
    elif(i % 4 != 0 and i % 4 != 2):
        for i in range(0, n):
            print('#', end='')

    