# 카카오 2020
# 괄호 변환

# '()', ')(' 로만 이루어진 문자열이 있고 ), ( 의 개수가 같다면 균형잡힌 괄호문자열
# 그리고 그 괄호의 짝도 모두 맞을 경우에는 올바른 괄호 문자열 이라고 한다

# 1.입력이 빈 문자열인 경우, 빈 문자열을 반환한다   (o)
# 2. 문자열을 두개의 균형잡힌 문자열 u, v 로 분리한다. 이 때 u는 균형잡힌 괄호 문자열로 더이상 분리할수 없어야 한다. v는 빈문자열이어도 된다
# 3. 문자열 u가 올바른 괄호 문자열이라면 문자열 v에 대해 1단계부터 다시 수행한다
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환한다
# 4. 문자열 u가 올바른 괄호 문자열이 아니라면
# 4-1. 빈 문자열에 첫 번쨰 문자로 '(' 를 붙인다
# 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다
# 4-3. ')'를 다시 붙인다
# 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다
# 4-5. 생성된 문자열을 반환한다


# 균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    count = 0  # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# 올바른 괄호 문자열인지 판단


def check_proper(p):
    count = 0  # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:   # 쌍이 맞지 않은 경우 False 반환
                return False
            count -= 1
    return True  # 쌍이 맞는 경우에 True 반환


def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # 올바른 괄호 문자열이면, v에 대해 함수를 수행한 결과를 붙여 반환한다
    if check_proper(u):
        answer = u + solution(v)
    # 올바른 괄호 문자열이 아니라면 아래의 과정을 수행한다
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])  # 첫번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
