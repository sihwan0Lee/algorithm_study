# 프로그래머스 더 맵게

# 먼저 힙에 대하여 알아보자
# 힙은 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전 이진트리를 기본으로 한다.

# A가 B의 노드이면 A의 키값과 B의 키값 사이에는 대소 관계가 성립한다.
# 최소 힙 : 부모 노드의 키 값이 자식 노드의 키 값보다 항상 작은 힙
# 최대 힙 : 부모 노드의 키 값이 자식 노드의 키 값보다 항상 큰 힙
# 이러한 구조로 힙에서는 항상 가장 낮거나 높은 우선 순위를 가지는 노드가 항상 루트에 오게 된다.

# 파이썬에서는 heapq 모듈을 제공해준다.
# heapq(priority queue) 우선순위 큐
# 내부적으로는 k번째 원소는 항상 자식 원소들(2k+1, 2k+2) 보다 작거나 같은 최소 힙의 형태로 정렬된다.

# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.
# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )

# 문제로 돌아와서
# 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶다.
# 가장 지수가 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식으로 만든다
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞는다.
# 이 문제는 그냥 힙큐를 안쓰고 배열로 풀어도 풀리긴하지만, 효율성에서 통과가 안되는 문제인듯하다
# scoville = [1, 2, 3, 9, 10, 12]
# K = 7


def solution(scoville, K):
    import heapq
    count = 0
    heapq.heapify(scoville)

    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) <= 0:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        count += 1
    return count


print(solution([1, 2, 3, 9, 10, 12], 7))


# 힙을 안쓰고 pop의 속도를 더빨리 처리하고싶어서 reverse로 정렬한후 해봤다.
def solution2(scoville, K):
    count = 0
    scoville.sort(reverse=True)

    while scoville:
        first = scoville.pop()
        if first >= K:
            break
        if len(scoville) <= 0:
            return -1
        second = scoville.pop()
        scoville.append(first + second * 2)
        count += 1
        scoville.sort(reverse=True)
    return count


print(solution2([1, 2, 3, 9, 10, 12], 7))

# 결과는 "실패 (시간 초과)" 였다.

# 이번 문제의 포인트는 heapq를 통해서 최소(최대)값을 빠르게 구하여 연산 속도를 높히는 것아니었을까.ㅎ
