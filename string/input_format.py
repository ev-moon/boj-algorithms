# Problem No. 5177

open_paren = {"(", "[", "{"}
close_paren = {")", "]", "}"}
comma = [",", ";"]

# 64ns
def parse_line(line):
    line = line.strip()
    result = []
    space = False
    for char in line:
        if char == " ":
            space = True
            continue
        if space and (not result or result[-1].isalnum()):
            result.append(" ")
        space = False
        if char.isalnum():
            result.append(char.lower())
        else:
            if result and result[-1] == " ":
                result.pop()
            if char in open_paren:
                result.append("(")
            elif char in close_paren:
                result.append(")")
            elif char in comma:
                result.append(",")
            else:
                result.append(char)
    if space and (not result or result[-1].isalnum()):
        result.append(" ")
    return "".join(result)


num_cases = int(input())

for case in range(num_cases):
    equal = True
    parsed1 = parse_line(input())
    print("line 1:", parsed1)
    parsed2 = parse_line(input())
    print("line 2:", parsed2)
    if parsed1 != parsed2:
        equal = False

    print(f"Data Set {case+1}: {'equal' if equal else 'not equal'}\n")
