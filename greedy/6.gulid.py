# 모험가N명, 공포도가 N만큼 주어진다
# 공포도가 x인 모험가는 반드시 x명이상으로 구성한 모험가 그룹에 참여해야한다.
# 그룹 수를 "최대"로 만들어야 한다.
# 마을에 남아있는 모험가가 있어도 된다!!

# 그룹을 가장많이 만드려면 모험가중에 공포도가 낮은 애들부터 내보내면 될것같다.
# 그러려면 sort를 해야한다는 hint

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0
for i in data:
    count += 1   # 이건 현재 해당하는 그룹의 인원 수임.
    if count >= i:
        result += 1
        count = 0

print(result)
