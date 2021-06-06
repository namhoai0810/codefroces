line = int(input())

for i in range(line):
    wight, hight = map(int, input().split())
    with_tmp = wight * 2
    hight_tmp = hight * 2
    if(with_tmp > hight_tmp):
        if(wight > hight_tmp):
            print(wight*wight)
        else:
            print(hight_tmp*hight_tmp)
    else:
        if(hight > with_tmp):
            print(hight*hight)
        else:
            print(with_tmp*with_tmp)