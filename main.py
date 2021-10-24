n = int(input())
a = list(map(int, input().split()))
k = int(input())
for i in range(n):
    if a[i] == k:
        print(i)
    else:
        pass
