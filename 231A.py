problem = int(input())
count = 0
for problemset in range(problem):
    solution = input()
    if(solution.count('1') >= 2):
        count = count + 1
print(count)