number = int(input())
lucky_num = 0
num_lucky = 0

while(number > 0):
    lucky_num = number % 10
    # print(lucky_num)
    if(lucky_num == 4 or lucky_num == 7):
        num_lucky = num_lucky + 1

    number = int(number // 10)
    # print(number)

# print(num_lucky)
if(num_lucky == 4 or num_lucky == 7):
    print("YES")
else:
    print("NO")