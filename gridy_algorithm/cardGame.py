a,b = map(int,input().split())

answer = 0

for i in range(a):
    number = list(map(int,input().split()))
    minval = min(number)
    answer = max(answer,minval)
print(answer)
