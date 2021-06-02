line = int(input())
for item in range(line):
    number = int(input())
    s1 = s2 = 0
    if(number % 4 != 0):
        print("NO")
    else:
        print("YES")
        for i in range(2, number+1 , 2):
            print(i, end = " ")
            s1 = s1 + i
        for i in range(1, number - 1, 2):
            print(i, end=' ')
            s2 = s2 + i
        print(s1 - s2)