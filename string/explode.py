# Problem No. 9935

# 통과
import sys

input = sys.stdin.readline

string = input().strip()
key = input().strip()

stack = list()
for char in string:
    stack.append(char)
    if len(stack) >= len(key):
        match = True
        for j in range(-1, -len(key) - 1, -1):
            if stack[j] != key[j]:
                match = False
                break
        if match:
            for i in range(len(key)):
                stack.pop()
if not stack:
    print("FRULA")
else:
    print("".join(stack))


# Notable Solution -- 리스트 entry를 저렇게도 지울 수 있구나..!
# def main():
#     string = input().strip()
#     bomb = input().strip()
#     bombl = list(bomb)
#     b_last = bomb[-1]
#     bl = len(bomb)

#     ans = []
#     for l in string:
#         ans.append(l)
#         if b_last == l and bombl == ans[-bl:]:
#             del ans[-bl:]

#     print(''.join(ans) if ans else "FRULA")


# if __name__ == '__main__':
#     main()

# Time Exceeded
# while True:
#     start_length = len(start)
#     start = start.replace(key, "")
#     if start_length == len(start):
#         break
# if not start:
#     print("FRULA")
# else:
#     print(start)

# stack = list()
# popped = list()
# pos = s_idx = 0


# 2% wrong
# for idx, char in enumerate(string):
#     if char == key[0]:
#         if pos != 0:
#             stack.append((s_idx, pos))
#         pos = 1
#         s_idx = idx
#     elif char == key[pos]:
#         pos += 1
#     else:  # mismatch
#         stack = []
#         pos = 0
#     if pos == len(key):
#         if popped and popped[-1][0] + len(key) > s_idx:  # nested explode
#             last_entry = popped.pop()
#             popped.append((s_idx, last_entry[1] + 1))
#         else:
#             popped.append((s_idx, 1))
#         if stack:
#             s_idx, pos = stack.pop()
#         else:
#             pos = 0
# string = list(string)
# for start, length in popped:
#     string[start : start + length * len(key)] = "*" * length * len(key)
# string = "".join(string)
# answer = "".join(string.split("*"))
# if not answer:
#     print("FRULA")
# else:
#     print(answer)
