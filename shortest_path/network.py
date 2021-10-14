# Problem No. 1922
# MST -- Kruskal

import sys
from heapq import heappush, heappop


def kruskal(num_vertices, v_heap):
    clusters = {_: _ for _ in range(1, num_vertices + 1)}
    cluster_set = {_: {_} for _ in range(1, num_vertices + 1)}
    min_spanning_cost = 0
    while len(cluster_set) > 1:
        cost, start_v, end_v = heappop(v_heap)
        if clusters[start_v] != clusters[end_v]:
            to_add = clusters[start_v]
            to_delete = clusters[end_v]
            for vertex in cluster_set[to_delete]:
                clusters[vertex] = to_add
                cluster_set[to_add].add(vertex)
            del cluster_set[to_delete]
            min_spanning_cost += cost
    return min_spanning_cost


input = sys.stdin.readline

num_computers = int(input())
num_edges = int(input())

heap = []
for _ in range(num_edges):
    start_v, end_v, cost = map(int, input().strip().split())
    heappush(heap, (cost, start_v, end_v))
print(kruskal(num_computers, heap))
