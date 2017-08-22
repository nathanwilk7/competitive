import sys

W, P = sys.stdin.readline().split(' ')
W = int(W)
parts = [False] * 101

dists = list(map(int, sys.stdin.readline().split(' ')))
dists.insert(0, 0)
dists.append(W)

for i in range(len(dists) - 1):
    for j in range(i + 1, len(dists)):
        parts[dists[j] - dists[i]] = True

for i in range(1, len(parts)):
    if parts[i]:
        print(i)
