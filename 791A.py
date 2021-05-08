weight_Limak, weight_Bob = map(int, input().split())
weight_Bob_new = weight_Bob
weight_Limak_new = weight_Limak
year = 0
while(weight_Limak_new <= weight_Bob_new):
    weight_Bob_new = 2 * weight_Bob_new
    weight_Limak_new = 3 * weight_Limak_new
    year = year + 1

print(year)