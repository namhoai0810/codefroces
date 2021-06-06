line = int(input())
for i in range(line):
    number = int(input())
    line1 = list(map(int,input().split()))
    line2 = list(map(int,input().split()))
    min1 = min(line1)
    min2 = min(line2)
    m = 0
    c = 0
    for i in range(number):
        if(line1[i] > min1 and line2[i] > min2):
            m = min(line1[i], line2[i])
            line1[i] = line1[i] - (m - min(min1,min2))
            line2[i] = line2[i] - (m - min(min1,min2))
            c = c + (m - min(min1,min2))
            if(line1[i] > min1):
                c = c + line1[i] - min1
                line1[i] = line1[i] - (line1[i] - min1)
            elif ((line2[i] > min2)):
                c = c + line2[i] - min2
                line2[i] = line2[i] - (line2[i] - min2)
        elif (line1[i] == min1 and line2[i] > min2):
            c = c +  line2[i] - min2
            line2[i] -= line2[i] - min2;
        elif (line1[i] > min1 and line2[i] == min2):
            c += line1[i] - min1
            line1[i] -= line1[i] - min1
        
    print(c)
