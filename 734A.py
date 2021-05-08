row = int(input())
men_Win = input()
A_win = 0
D_win = 0
for i in range(0, row):
    if(men_Win[i] == 'A'):
        A_win = A_win + 1
    elif(men_Win[i] == 'D'):
        D_win = D_win + 1
    else:
        pass

if(A_win > D_win):
    print("Anton")
elif(D_win > A_win):
    print("Danik")
else:
    print("Friendship")