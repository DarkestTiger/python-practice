# 변수로 더 직관적인 문자열 만들기
# 예를 들어 아래 for문을 살펴보자.

scores = [
    {'name':'영수','score':70},
    {'name':'영희','score':65},
    {'name':'기찬','score':75},
    {'name':'희수','score':23},
    {'name':'서경','score':99},
    {'name':'미주','score':100},
    {'name':'병태','score':32}    
]

for s in scores:
    name = s['name']
    score = str(s['score'])
    print(name,score)

# 이렇게 하면 이름과 점수가 모두 출력된다.

# 그런데 반대로 이렇게도 출력할수있다.
for s in scores:
    name = s['name']
    score = str(s['score'])
    print(name+'는 '+score+'점 입니다')

    # 변수  name 과 문자열 '는 ' 과 변수 score 과 문자열 '점 입니다'를 더하기로 이어서 출력할수있다.
    # 그런데 매번 모두 이렇게 하려고 하면 매우 번거로울것이다.
    
    # 그래서 우리는 f=string이라는것을 시도 해볼 수 있다.

for s in scores:
    name = s['name']
    score = str(s['score'])
    print(f'{name}은 {score}점입니다')

    # 이렇게 하면 더 간단하게 출럭할수있다.