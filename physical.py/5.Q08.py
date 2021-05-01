# 문자열 재정렬

# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다.
# 알파벳을 오름차순으로 정렬하여 이어서 출력하고 그 뒤에 숫자의 모든 합을 출력한다

def solution(data):
    result = []
    value = 0
    for i in data:
        if i.isalpha():
            result.append(i)
        else:
            value += int(i)

    result.sort()

    if value != 0:
        result.append(str(value))

    print(''.join(result))


print(solution("K1KA5CB7"))
