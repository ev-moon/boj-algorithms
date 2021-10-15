# Problem No. 2887

import sys

input = sys.stdin.readline

num_planets = int(input().rstrip())
x_coord_list = []
y_coord_list = []
z_coord_list = []
for i in range(num_planets):
    x_coord, y_coord, z_coord = map(int, input().rstrip().split())
    x_coord_list.append((x_coord, i))
    y_coord_list.append((y_coord, i))
    z_coord_list.append((z_coord, i))

x_coord_list.sort()
y_coord_list.sort()
z_coord_list.sort()


def get_min_distance(coord_a, coord_b):
    min_dist = float("inf")
    for c_a, c_b in zip(coord_a, coord_b):
        min_dist = min(min_dist, abs(c_a - c_b))
    return min_dist


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edges = []

for i in range(num_planets - 1):
    edges.append(
        (
            x_coord_list[i + 1][0] - x_coord_list[i][0],
            (x_coord_list[i][1], x_coord_list[i + 1][1]),
        )
    )
    edges.append(
        (
            y_coord_list[i + 1][0] - y_coord_list[i][0],
            (y_coord_list[i][1], y_coord_list[i + 1][1]),
        )
    )
    edges.append(
        (
            z_coord_list[i + 1][0] - z_coord_list[i][0],
            (z_coord_list[i][1], z_coord_list[i + 1][1]),
        )
    )

edges.sort()
parent = [_ for _ in range(num_planets)]
total_cost = 0
for edge in edges:
    cost, (p_a, p_b) = edge
    if find_parent(parent, p_a) != find_parent(parent, p_b):
        union_parent(parent, p_a, p_b)
        total_cost += cost


print(total_cost)