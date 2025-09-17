n = int(input())
result=0

for i in range(1,n+1):
    add=0
    for j in range(1,i+1):
        add+=j
    result += add
print(result)
9/17
n = int(input())

for i in range(1,7):
    for j in range(1,7):
        if i+j == n:
            print(i,j)
