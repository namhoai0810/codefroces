
stone = int(input())
color = input()
sum = 0
for i in range(0,len(color)):
    if((i + 1) < len(color)):
        if(color[i] == color[i+1]):
            sum = sum + 1
    else:
        print(sum)

# print(len(string))
# for i in range(0,len(string)):
#     if((i+1) < len(string)):
#         print(i)
#     else:
#         break
    # if(string[i] == 'G'):
    #     break