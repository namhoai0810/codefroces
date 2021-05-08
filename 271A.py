year = int(input())
last_num = 0
secon_num = 0
thir_num = 0
for_num = 0
while(True):
    year = year + 1
    last_num = year % 10
    secon_num = (year // 10) % 10
    thir_num = (year // 100) % 10
    for_num = (year // 1000)
    if((last_num != secon_num) and (last_num != thir_num) and (last_num != for_num) and (secon_num != thir_num) and (secon_num != for_num) and (thir_num != for_num)):
        break
    

print(year)