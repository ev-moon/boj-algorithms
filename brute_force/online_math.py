# https://www.acmicpc.net/problem/19532

import sys

input = sys.stdin.readline
a_1, b_1, c_1, a_2, b_2, c_2 = map(int, input().strip().split())
y = (c_1 * a_2 - c_2 * a_1) // (b_1 * a_2 - b_2 * a_1)
x = (c_1 * b_2 - c_2 * b_1) // (a_1 * b_2 - a_2 * b_1)
print(x, y)