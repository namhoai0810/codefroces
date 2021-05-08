hang, time_hang = map(int, input().split())
str_hang = input()
list_new = list(str_hang)
j = 0
for i in range(0, time_hang):
    j = 0
    while(j < len(list_new)):
        if((j+1) < len(list_new)):
            if(list_new[j] == "B" and list_new[j+1] == "G"):
                list_new[j] = "G"
                list_new[j+1] = "B"
                j = j + 1
        j = j + 1
for i in range(0, len(list_new)):
    print(list_new[i], end='')
