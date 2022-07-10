# rjust
# 오른쪽으로 정렬하도록 도와주며, "문자열".rjust(공백의수, 공백을 메꿀 문자) 로 사용한다.
x = "aa".rjust(7, "b")
print(x)

# y = 1.rjust(5, 2) -> 문자만 가능하다. 숫자형태는 되지 않는다.
# TypeError: The fill character must be a unicode character, not int
y = "1".rjust(5, "2")
print(y)

# ljust  는 그와 반대로 왼쪽부터 정렬하도록 하는 것이다.

# center
c = "a".center(7, "0")
print(c)

d = "a".center(8, "0")
print(d)
# 짝수의 경우에는 왼쪽이 먼저 채워지는 듯하다.