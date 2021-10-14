# Problem No. 1931

import sys

input = sys.stdin.readline

num_meetings = int(input().strip())
meetings = []
final_end = 0
for _ in range(num_meetings):
    start, end = map(int, input().strip().split())
    final_end = max(final_end, end + 1)
    meetings.append((start, end))
meetings.sort(key=lambda x: (x[1], x[0]))

max_meetings = [0] * final_end
m_idx = 0  # counter for meetings
for idx in range(final_end):
    max_meetings[idx] = max_meetings[idx - 1]
    while m_idx < num_meetings and idx == meetings[m_idx][1]:
        max_meetings[idx] = max(
            max_meetings[meetings[m_idx][0]] + 1, max_meetings[idx - 1]
        )
        m_idx += 1

print(max_meetings[-1])