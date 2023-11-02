from sys import argv

n, m = list(map(int, argv[1:]))

i = 1
while True:
    print(i, end='')
    i = 1 + (i + m - 2) % n
    if i == 1:
        break
print()



