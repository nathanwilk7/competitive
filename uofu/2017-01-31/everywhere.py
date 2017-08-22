import sys

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    cities = set()
    for j in range(n):
        cities.add(sys.stdin.readline().strip())
    print(len(cities))
