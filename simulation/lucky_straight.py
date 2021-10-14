num = input().rstrip()

cut_len = len(num) // 2
upper, lower = num[:cut_len], num[cut_len:]
upper_sum = lower_sum = 0
for a, b in zip(upper, lower):
    upper_sum += int(a)
    lower_sum += int(b)

if upper_sum == lower_sum:
    print("LUCKY")
else:
    print("READY")