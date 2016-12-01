def solution(string, markers):
    l = string.split("\n")
    for i in range(len(l)):
        for m in markers:
            pos = l[i].find(m)
            if pos != -1:
                l[i] = l[i][:pos].rstrip()

    return '\n'.join(l)

print solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])

# other solutions
def solution2(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)