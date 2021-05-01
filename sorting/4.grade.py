def solution(scores):
    # 자기 점수를 가지는 행을 만들기 위해 행과 열을 뒤바꿈
    new_data = [[] for i in range(len(scores))]
    answer = []
    grade = []
    for score in scores:
        for i in range(len(new_data)):
            a = score.pop(0)
            new_data[i].append(a)
    for i in range(len(new_data)):
        print(new_data[i], len(new_data[i]))
        # 유일할때는 그걸 제외하고 계산
        if new_data[i][i] == max(new_data[i]) or min(new_data[i]) and new_data[i].count(min(new_data[i])) == 1:

            answer.append(
                (sum(new_data[i]) - new_data[i][i]) / (len(new_data[i])-1))

        # 유일하지 않으면  포함하고 계산
        elif new_data[i][i] == max(new_data[i]) or min(new_data[i]) and new_data[i].count(min(new_data[i])) > 1:

            answer.append(sum(new_data[i]) / len(new_data[i]))

        # 자기평가가 최고나 최저가 아닐경우
        elif new_data[i][i] != max(new_data[i]) or min(new_data[i]):
            answer.append(sum(new_data[i]) / len(new_data[i]))

    for i in answer:
        if i >= 90:
            grade.append("A")
        elif i >= 80 and i < 90:
            grade.append("B")
        elif i >= 70 and i < 80:
            grade.append("C")
        elif i >= 50 and i < 70:
            grade.append("D")
        elif i < 50:
            grade.append("F")
    return ''.join(grade)


print(solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [
      47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
# print(solution([[50,90],[50,87]]))
