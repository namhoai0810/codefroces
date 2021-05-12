str = input()[1:-1].split(", ")
if(str == ['']):
    print('0')
else:
    print(len(set(str)))
# print(str)