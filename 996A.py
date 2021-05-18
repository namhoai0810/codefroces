money = int(input())
bill = [100, 20, 10, 5 ,1]
count = 0
for item in range(0, len(bill)):
    count = count + int(money/(bill[item]))
    money = money - bill[item] * int((money/bill[item]))

print(count)
