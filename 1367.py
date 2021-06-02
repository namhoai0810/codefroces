line = int(input())

for item in range(line):
    arr = input()
    string = ""
    i = 0
    while(True):
        if(i == len(arr)):
            break
        elif(i == 0):
            string =  string + arr[i]
        elif((i + 1) <= (len(arr) - 1)):
            if(arr[i] == arr[i+1]):
                string = string + arr[i]
                i = i + 1
        i = i + 1
    string = string + arr[-1]    

    print(string)