string = input()
case_upper = 0
case_lower = 0
for i in range(0, len(string)):
    if(string[i].isupper()):
        case_upper = case_upper + 1
        # print(case_upper)
    
# print(case_upper)
case_lower = len(string) - case_upper
# print(case_lower)

if(case_lower >= case_upper):
    print(string.lower())
else:
    print(string.upper())
    
