n, m = map(int, input().split())

massive = [x for x in range(1, n + 1)]

round_massive = []

last_num = 1

while True:
    print(last_num, end='')
    if last_num - 1 + m >= n:
        if last_num - 1 + m == n:
            round_massive.extend(massive[last_num - 1:last_num - 1 + m])
            last_num = massive[-1]

            if round_massive[0] == round_massive[-1]:
                break
            continue

        else:
            peregruz = (last_num - 1 + m) % n
            round_massive.extend(massive[last_num - 1:])
            round_massive.extend(massive[:peregruz])
            last_num = peregruz

            if round_massive[0] == round_massive[-1]:
                break
            continue

    round_massive.extend(massive[last_num - 1:last_num - 1 + m])
    last_num = last_num - 1 + m
    if round_massive[0] == round_massive[-1]:
        break
print()


# Решение со stack overflow с модульной арифметикой :) -->

# n, m = map(int, input().split())
#
# i = 1
# while True:
#     print(i, end='')
#     i = 1 + (i + m - 2) % n
#     if i == 1:
#         break
# print()



