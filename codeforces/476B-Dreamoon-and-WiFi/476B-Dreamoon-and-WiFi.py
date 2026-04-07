def calc(idx, s):
    global res

    if idx == len(s):
        # print(temp)
        if temp.count("+") == p:
            res += 1
        return

    if s[idx] != "?":
        temp.append(s[idx])
        calc(idx+1, s)
        temp.pop()
    else:
        temp.append("+")
        calc(idx+1, s) 
        temp.pop()
        temp.append("-")
        calc(idx+1, s)
        temp.pop()

calc(0, b)
print(res/ans)