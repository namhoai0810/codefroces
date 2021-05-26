
case = int(input())
for i in range(0, case):
    n = int(input())
    number = set(map(int, input().split(" ")))
    string_number = list(number)
    string_number.sort(reverse=True)
    # print(string_number)
    if(len(string_number) == 1):
        print("YES")
    else:
        flag = 0
        for item in range(0,len(string_number) - 1):
            
            if(string_number[item] - string_number[item+1] != 1):
                flag = 1
                break
            else:
                flag = 0
        # print(flag)
        print("YES") if flag == 0 else print("NO")
