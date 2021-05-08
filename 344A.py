n = int(input())

last_row = "00"
sum = 0
for i in range(n):
    manget = input()
    if(manget != last_row):
        sum = sum + 1
        last_row = manget

print(sum)