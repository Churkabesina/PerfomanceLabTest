from sys import argv

paths = argv[1:]

krug_center = []
krug_radius = 0

points = []

with open(paths[0], 'r', encoding='UTF-8') as krug_file:
    krug_center.extend(map(float, krug_file.readline().rstrip('\n').split()))
    krug_radius = int(krug_file.readline().rstrip('\n'))

with open(paths[1], 'r', encoding='UTF-8') as points_file:
    for i in points_file:
        points.append(i.rstrip())

for point in points:
    point = list(map(float, point.split()))
    distance = ((point[0] - krug_center[0])**2 + (point[1] - krug_center[1])**2)**0.5
    if distance == krug_radius:
        print(0)
        continue
    if distance < krug_radius:
        print(1)
        continue
    if distance > krug_radius:
        print(2)
        continue
