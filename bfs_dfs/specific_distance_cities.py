# Problem No. 18352

from collections import defaultdict, deque
import sys

input = sys.stdin.readline


def BFS(roads, start, target_distance):
    queue = deque([[start, 0]])
    min_dist = defaultdict(lambda: float("inf"))
    while queue:
        city, dist = queue.popleft()
        if dist > target_distance:
            continue
        min_dist[city] = min(min_dist[city], dist)
        for next_city in roads[city]:
            if dist + 1 < min_dist[next_city]:
                queue.append([next_city, dist + 1])
    return min_dist


num_cities, num_roads, target_distance, start = map(int, input().rstrip().split())
roads = defaultdict(set)
for _ in range(num_roads):
    _start, _end = map(int, input().rstrip().split())
    roads[_start].add(_end)
min_dist = BFS(roads, start, target_distance)
answer_cities = [key for key, val in min_dist.items() if val == target_distance]
if answer_cities:
    print(*sorted(answer_cities), sep="\n")
else:
    print(-1)
