def solution(N):
    make_bin = bin(N)[2:]

    index_one = []
    bin_gap = []

    for i in range(len(make_bin)):
        if make_bin[i] == "1":
            index_one.append(i)
    if len(index_one) < 2:
        return 0
    else:
        for j in range(len(index_one) - 1):
            bin_gap.append(index_one[j+1] - index_one[j] - 1)

    return max(bin_gap)


# print(solution(1041))


def solution2(N):
    make_bin = bin(N)[2:]
    zero = []
    for i in range(len(make_bin) + 2):
        count = 0
        # 1이 나타나면 다음 1이 나타날때까지 카운트를 올린다.
        if make_bin[i] == "1":
            while make_bin[i + 1] == "1":
                count += 1
                print(count)


print(solution2(1041))
