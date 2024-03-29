import sys

sys.stdin = open("traffic.in", "r")
sys.stdout = open("traffic.out", "w")

b = int(input())

info = []
status = []
ranges = []

for i in range(b):
    info.append(input().split(" "))
    status.append(info[i][0])
    ranges.append([eval(i) for i in info[i][1:3]])

x, y = 0, 0
x2, y2 = -69, -69

for i in range(len(ranges)):
    if status[i] == "none":
        if ranges[i][0] > x2:
            x2 = ranges[i][0]
        if ranges[i][1] < y2 or y2 == -69:
            y2 = ranges[i][1]
    if x2 != -69 and status[i] == "on":
        x2 += ranges[i][0]
        y2 += ranges[i][1]
    if x2 != -69 and status[i] == "off":
        x2 -= ranges[i][1]
        y2 -= ranges[i][0]
if x2 < 0:
    x2 = 0
if y2 < 0:
    y2 = 0

l = [x2, y2]

for i in range(len(ranges)):
    i = len(ranges) - i - 1
    if status[i] == "none":
        if ranges[i][0] > x2:
            x2 = ranges[i][0]
        if ranges[i][1] < y2:
            y2 = ranges[i][1]
    if status[i] == "off":
        x2 += ranges[i][0]
        y2 += ranges[i][1]
    if status[i] == "on":
        x2 -= ranges[i][1]
        y2 -= ranges[i][0]
if x2 < 0:
    x2 = 0
if y2 < 0:
    y2 = 0

print(x2, y2)
print(l[0], l[1])
