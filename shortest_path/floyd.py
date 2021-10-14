# Problem No. 11404

import sys

input = sys.stdin.readline

n_cities = int(input())
n_buses = int(input())
costs = [[float("inf")] * n_cities for _ in range(n_cities)]

for _ in range(n_buses):
    s, e, cost = map(int, input().split())
    costs[s - 1][e - 1] = min(costs[s - 1][e - 1], cost)
for i in range(n_cities):
    for j in range(n_cities):
        for k in range(n_cities):
            costs[j][k] = min(costs[j][k], costs[j][i] + costs[i][k])

for x in range(n_cities):
    for y in range(n_cities):
        if x == y:
            costs[x][y] = 0
        if costs[x][y] == float("inf"):
            costs[x][y] = 0

for row in costs:
    print(*row)
