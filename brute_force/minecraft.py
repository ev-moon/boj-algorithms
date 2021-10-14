# Problem No. 18111

from collections import defaultdict

row, col, blocks = map(int, input().split())

freq = defaultdict(int)
for _ in range(row):
    for block in map(int, input().split()):
        freq[block] += 1

keys = sorted(list(freq.keys()), reverse=True)
time = -1
for target_level in range(min(keys[0], 256), min(255, keys[-1] - 1), -1):
    extra_blocks = 0
    to_fill = 0
    for level in keys:
        if level > target_level:
            extra_blocks += (level - target_level) * freq[level]
        elif level < target_level:
            to_fill += (target_level - level) * freq[level]
    if to_fill <= blocks + extra_blocks:  # possible level
        if time == -1:  # first iteration
            time = min(blocks, to_fill) + max(to_fill - blocks, 0) + extra_blocks * 2
            cheap_level = target_level
        else:
            new_time = min(
                time, min(blocks, to_fill) + max(to_fill - blocks, 0) + extra_blocks * 2
            )
            if time > new_time:
                cheap_level = target_level
                time = new_time

print(time, cheap_level)
