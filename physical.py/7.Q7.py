# 럭키 스트레이트
# 현재 캐릭터의 점수 N
# 자릿수 기준으로 점수를 반으로 나눠 왼쪽 부분의 각 자릿수의 합과 오른쪽 자릿수의 합을 더한 값이 동일할떄가 특정 조건이다
# N이 주어지면 럭키스트레이트를 쓸수 있는지 판단하는 프로그램을 작성 하시오
# N은 짝수 형태로만 주어진다.

n = input()
sum_l = 0
sum_r = 0
# 왼쪽
for i in range(len(n) // 2):
    sum_l += int(n[i])

# 오른쪽
for j in range(len(n)//2, len(n)):
    sum_r += int(n[j])

if sum_l - sum_r == 0:
    print('LUCKY')
else:
    print('READY')
