string1 = input()
string2 = input()
string3 = ""
for item in range(0, len(string1)):
    if(string1[item] == string2[item]):
        string3 = string3 + "0"
    else:
        string3 = string3 + "1"

print(string3)
