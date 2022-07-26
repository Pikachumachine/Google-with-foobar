def solution(s):
    # Your code here
    salute_total = 0
    for i in range(len(s)):
        if s[i] == ">":
            salute = 0
            for j in range(i + 1, len(s)):
                if s[j] == "<":
                    salute += 1
            if salute == 0:
                break
            salute_total += salute
    return salute_total*2
