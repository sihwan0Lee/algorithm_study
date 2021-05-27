# () = Parenthesis
# {} = Brace
# [] = Bracket
# <> = Chevron


def solution(s):
    s = [i for i in s]
    count = 0
    if s[0] == ")":
        return False
    for i in range(len(s)):
        if s[i] == "(":
            count += 1
        else:
            count -= 1
        print(count)
    if count == 0:
        return True

# print(solution("(())()"))

# 84.6/100


def solution(s):
    Q = []
    for i in s:
        if i == '(':
            Q.append('(')
        elif len(Q) >= 1 and i == ')':
            Q.pop()
        print(Q)
    if len(Q) == 0:
        return True
    else:
        return False


print(solution("(())()"))
# 92.3/ 100.0


def solution(s):
    Q = []
    if s[0] == ")":
        return False
    for i in s:

        if i == '(':
            Q.append('(')
        elif len(Q) >= 1 and i == ')':
            Q.pop()
    if len(Q) == 0:
        return True
    else:
        return False

# 100.0/100.0
