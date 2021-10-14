# Problem No. 1655
# Utilize Double Heaps(Minheap and Maxheap)

import sys, heapq

input = sys.stdin.readline

n_numbers = int(input().strip())
min_heap = list()
max_heap = list()
heapq.heapify(min_heap)
heapq.heapify(max_heap)
for it in range(n_numbers):
    to_push = int(input().strip())
    if len(max_heap) - len(min_heap) == 1:
        if max_heap and to_push < -max_heap[0]:
            heapq.heappush(min_heap, -heapq.heapreplace(max_heap, -to_push))
        else:
            heapq.heappush(min_heap, to_push)
    else:
        if min_heap and to_push > min_heap[0]:
            heapq.heappush(max_heap, -heapq.heapreplace(min_heap, to_push))
        else:
            heapq.heappush(max_heap, -to_push)
    if len(max_heap) > len(min_heap):
        print(-max_heap[0])
    else:
        print(min(-max_heap[0], min_heap[0]))