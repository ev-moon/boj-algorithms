# Problem No. 11779

import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def trace_path(backtrack, end, start):
    backtrack[start] = None  # stop looping when start=end
    path = [end]
    while backtrack[end]:
        path.append(backtrack[end])
        end = backtrack[end]
    return path[::-1]


def dijkstra(graph, start, end):
    min_dist = {_: float("inf") for _ in range(1, len(graph) + 1)}
    min_dist[start] = 0
    backtrack = {_: None for _ in range(1, len(graph) + 1)}
    heap = [(0, start)]
    while heap:
        cost, cur_node = heappop(heap)
        if cost > min_dist[cur_node]:
            continue
        for connect_v, connect_cost in graph[cur_node - 1].items():
            if cost + connect_cost < min_dist[connect_v]:
                min_dist[connect_v] = cost + connect_cost
                heappush(heap, (cost + connect_cost, connect_v))
                backtrack[connect_v] = cur_node
    return min_dist[end], backtrack


num_cities = int(input())
num_edges = int(input())

graph = [dict() for _ in range(num_cities)]
for _ in range(num_edges):
    start_v, end_v, cost = map(int, input().split())
    # construct graph
    if end_v not in graph[start_v - 1]:
        graph[start_v - 1][end_v] = cost
    else:
        graph[start_v - 1][end_v] = min(graph[start_v - 1][end_v], cost)
q_start, q_end = map(int, input().split())
cost, backtrack = dijkstra(graph, q_start, q_end)
path = trace_path(backtrack, q_end, q_start)
print(cost)
print(len(path))
print(*path)