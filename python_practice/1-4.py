"""
문제 4 Range advanced
1부터 15까지 짝수 * 10, 홀수는 그대로 list에 추가 후 출력
"""
result = []

for i in range(1,16):
    if i % 2 == 0:
        a = i * 10
        result.append(a)
    if i % 2 == 1:
        result.append(i)

print(result)