# Problem No. 1561

import sys

input = sys.stdin.readline


def solution():
    num_people, num_rides = map(int, input().split())
    ride_times = list(map(int, input().split()))
    low = 0
    high = 30 * num_people
    if num_people < num_rides:
        return num_people

    while low <= high:
        cnt = num_rides
        mid = (low + high) // 2
        for idx, time in enumerate(ride_times):
            cnt += mid // time
        if cnt >= num_people:
            t = mid
            high = mid - 1
        else:
            low = mid + 1
    cnt = num_rides
    for time in ride_times:
        cnt += (t - 1) // time
    for idx, time in enumerate(ride_times):
        if t % time == 0:
            cnt += 1
        if cnt == num_people:
            return idx + 1


print(solution())
