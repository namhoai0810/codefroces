number = int(input())
if(number % 2 == 0) :
    cnt = int(number / 2);
    print(cnt);
    for i in range(1, cnt+1):
        print("2",end=" ")
else:
    cnt = int(number / 2);
    print(cnt);
    for i in range(1, cnt):
        print("2", end=" ");
    print("3");