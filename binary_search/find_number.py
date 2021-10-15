# https://www.acmicpc.net/problem/1920

import sys

input = sys.stdin.readline

n = input().strip()
members = set()
for num in map(int, input().strip().split()):
    members.add(num)

m = input().strip()
for cand in map(int, input().strip().split()):
    if cand in members:
        print(1)
    else:
        print(0)