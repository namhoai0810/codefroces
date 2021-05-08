n = int(input())
string = ""
for i in range(1, n):
    if(i % 2 == 1):
        string = string + "I hate that "
    else:
        string = string + "I love that "        
if(n % 2 == 0):
    string = string + "I love it "
if(n % 2 == 1):
    string = string + "I hate it"

print(string)