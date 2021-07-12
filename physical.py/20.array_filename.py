# 카카오 2018 파일명정렬

# 파일을 HEAD, NUMBER, TAIL 로 나누기
import re


def solution(files):
    arr = [re.split(r"([0-9]+)", file) for file in files]
    print(arr)
    sort = sorted(arr, key=lambda x: (x[0].lower(), int(x[1])))
    print(sort)
    return ["".join(s) for s in sort]


print(solution(["img12.png", "img10.png", "img02.png",
                "img1.png", "IMG01.GIF", "img2.JPG"]))

# 내 평소 약점들의 결정체 : regex , key = lambda  왜 람다는 볼때마다 새롭냐.
