a = int(input())
i = 2
if a % i == 0:
    print(i)
else:
    while a % i != 0:
        i = i + 1
    print(i)
