lst_4 = list(map(int, input().split()))
lst_4.sort()
number1 = lst_4[3] - lst_4[0]
number2 = lst_4[3] - lst_4[1]
number3 = lst_4[3] - lst_4[2]
print("%d %d %d"%(number1,number2,number3))