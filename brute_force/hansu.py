# Problem No. 1065
number = int(input().strip())
answer = 0

answer += min(99, number)
for i in range(100, number + 1):
    string = str(i)
    gap = int(string[1]) - int(string[0])
    match = True
    for idx, char in enumerate(string[:-1]):
        if int(string[idx + 1]) - int(char) != gap:
            match = False
            break
    if match:
        answer += 1
print(answer)