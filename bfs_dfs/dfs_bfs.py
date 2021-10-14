# Problem No. 1260

from collections import deque
import sys

input = sys.stdin.readline

num_nodes, num_edges, start_node = map(int, input().strip().split())
graph = {_: set() for _ in range(1, num_nodes + 1)}

for _ in range(num_edges):
    start, end = map(int, input().strip().split())
    graph[start].add(end)
    graph[end].add(start)

# DFS Traversal
stack = [start_node]
dfs_traversed = []
while stack:
    cur_node = stack.pop()
    if cur_node not in dfs_traversed:
        dfs_traversed.append(cur_node)
        for c_node in sorted(graph[cur_node], reverse=True):
            if c_node not in dfs_traversed:
                stack.append(c_node)
print(*dfs_traversed)

# BFS Traversal
queue = deque([start_node])
bfs_traversed = []
while queue:
    cur_node = queue.popleft()
    if cur_node not in bfs_traversed:
        bfs_traversed.append(cur_node)
        for c_node in sorted(graph[cur_node]):
            if c_node not in bfs_traversed:
                queue.append(c_node)
print(*bfs_traversed)