"""
문제
해당 함수는 자연수 1개를 받음
1부터 해당 자연수까지 더하는 함수를 만드세요

자연수 10의 경우
결과 값 55

return 여부 비교
"""
def sum(num):
    return num * (num+1) // 2

print(sum(10))