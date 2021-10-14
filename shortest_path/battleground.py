# Problem No. 14938

import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def dijkstra(start_node, graph):
    min_dist = {i: float("inf") for i in range(1, len(graph) + 1)}
    heap = [(0, start_node)]
    while heap:
        dist, node = heappop(heap)
        if min_dist[node] < dist:
            continue
        min_dist[node] = dist
        for connect_node, connect_dist in graph[node - 1]:
            if dist + connect_dist < min_dist[connect_node]:
                heappush(heap, (connect_dist + dist, connect_node))
    return min_dist


num_nodes, search_range, num_edges = map(int, input().strip().split())
items = list(map(int, input().strip().split()))
graph = [[] for _ in range(num_nodes)]
for _ in range(num_edges):  # create graph
    start, end, dist = map(int, input().split())
    graph[start - 1].append((end, dist))
    graph[end - 1].append((start, dist))
max_items = 0
for node in range(1, num_nodes + 1):
    cur_items = 0
    min_dist = dijkstra(node, graph)
    for node, dist in min_dist.items():
        if dist <= search_range:
            cur_items += items[node - 1]
    max_items = max(max_items, cur_items)
print(max_items)