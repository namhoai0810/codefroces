line = int(input())
for i in range(0, line):
    lst_split = list()
    number = int(input())
    if(number % 10 != 0):
        ans = number % 10
        lst_split.append(ans)
        number = number - ans
    if(number % 100 != 0):
        ans = number % 100
        lst_split.append(ans)
        number = number - ans
    if(number % 1000 != 0):
        ans = number % 1000
        lst_split.append(ans)
        number = number - ans
    if(number % 10000 != 0):
        ans = number % 10000
        lst_split.append(ans)
        number = number - ans
    if(number == 10000 and number >= 10000):
        lst_split.append(number)

    print(len(lst_split))
    for item in lst_split:
        print(item, end =" ")
    print()