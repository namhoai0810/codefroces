number, subtra = map(int, input().split())


# print(string_number[-1])
for i in range(0, subtra):
    if(number > 0 and number % 10 == 0):
        number = number / 10
    elif(number < 0):
        break
    else:
        number = number - 1
        
print (int(number))