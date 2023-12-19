b = int(input())
info = []
status = []
ranges = []

for i in range(b):
    info.append(input().split(" "))
    status.append(info[i][0])
    ranges.append([eval(i) for i in info[i][1:3]])

x, y = 0, 0
x2, y2 = -1, -1

for i in range(len(ranges)):
    if x2 != -1 and status[i] == "on":
        x2 += ranges[i][0]
        y2 += ranges[i][1]
    if x2 != -1 and status[i] == "off":
        x2 -= ranges[i][1]
        y2 -= ranges[i][0]
    if status[i] == "none":
        if ranges[i][0] > x2:
            x2 = ranges[i][0]
        if ranges[i][1] < y2 or y2 == -1:
            y2 = ranges[i][1]

print(f"ENDING CARS: {x2}, {y2}")

for i in range(len(ranges)):
    if x2 != -1 and status[i] == "on":
        x2 -= ranges[i][0]
        y2 -= ranges[i][1]
    if x2 != -1 and status[i] == "off":
        x2 += ranges[i][1]
        y2 += ranges[i][0]

print(f"STARTING CARS: {x2}, {y2}")
