n = int(input())
sum = 0
for item in range(0, n):
    string = input()
    if(string == "Icosahedron"):
        sum = sum + 20
    elif(string == "Tetrahedron"):
        sum = sum + 4
    elif(string == "Cube"):
        sum = sum + 6
    elif(string == "Octahedron"):
        sum = sum + 8
    elif(string == "Dodecahedron"):
        sum = sum + 12
   
print(sum)