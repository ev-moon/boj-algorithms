# Problem No. 1753

import sys
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstra(num_nodes, graph, start):
    min_cost = {i: float("inf") for i in range(1, num_nodes + 1)}
    heap = [(0, start)]
    while heap:
        cost, node = heappop(heap)
        if cost > min_cost[node]:
            continue
        min_cost[node] = cost
        for connect_node, connect_cost in graph[node].items():
            if cost + connect_cost < min_cost[connect_node]:
                heappush(heap, (cost + connect_cost, connect_node))
    return min_cost


num_nodes, num_edges = map(int, input().strip().split())
start_node = int(input().strip())
graph = defaultdict(dict)
for _ in range(num_edges):  # construct graph
    start, end, cost = map(int, input().split())
    if end in graph[start]:
        graph[start][end] = min(graph[start][end], cost)
    else:
        graph[start][end] = cost
min_cost = dijkstra(num_nodes, graph, start_node)
for i in range(1, num_nodes + 1):
    if min_cost[i] == float("inf"):
        print("INF")
    else:
        print(min_cost[i])
