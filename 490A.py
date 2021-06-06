student = int(input())
lst = list(map(int, input().split()))

min_team = min(lst.count(1),min(lst.count(2),lst.count(3)))
print(min_team)

if(min_team > 0):
    x = lst.index(1)
    y = lst.index(2)
    z = lst.index(3)
    for i in range(min_team):
        print("%d %d %d"%(lst.index(1,x,student) + 1,lst.index(2,y,student) + 1, lst.index(3,z,student) + 1))
        x = lst.index(1,x,student) + 1
        y = lst.index(2,y,student) + 1
        z = lst.index(3,z,student) + 1
        
        
