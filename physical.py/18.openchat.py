# 카카오 2019 오픈채팅방

# 문제의 정확한 이해가 가장 중요!!

# 닉네임 변경방법 :
# 1. 채팅방을 나간 후 새로운 닉네임으로 들어온다.
# 2. 채팅방 안에서 닉네임을 변경한다.

# 닉네임을 변경하면 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다.
# 채팅방은 중복 닉네임을 허용한다.

# 채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열이 주어지면
# 모든 기록이 처리된 후, 최종적으로 방을 개설한 사함이 보게되는 메세지를 문자열 로 리턴하라

def solution(record):
    d = dict()
    r = []
    for rec in record:
        a = rec.split()
        if a[0] == 'Enter' or a[0] == 'Change':
            d[a[1]] = a[2]
    for i in record:
        a = i.split()
        print(a)
        if a[0] == 'Enter':
            r.append(d[a[1]] + '님이 들어왔습니다.')
        elif a[0] == 'Leave':
            r.append(d[a[1]] + '님이 나갔습니다.')
    return r


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
