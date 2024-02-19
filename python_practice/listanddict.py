# 순서가 있는, 다른 자료형들의 모임!
a = [1, 5, 2]
b = [3, "a", 6, 1]
c = []
d = list()
e = [1, 2, 4, [2, 3, 4]]

# 리스트의 길이도 len() 함수를 사용해서 잴 수 있어요.
a = [1, 5, 2]
print(len(a))   # 3

b = [1, 3, [2, 0], 1]
print(len(b))   # 4

#순서가 있기 때문에, 문자열에서처럼 인덱싱과 슬라이싱을 사용할 수 있습니다!
a = [1, 3, 2, 4]
print(a[3])  # 4
print(a[1:3]) # [3, 2]
print(a[-1]) # 4 (맨 마지막 것)

# 리스트의 요소가 리스트라면? 중첩해서!
a = [1, 2, [2, 3], 0]
print(a[2])      # [2, 3]
print(a[2][0])   # 2

# 더하기
a = [1, 2, 3]
a.append(5)
print(a)     # [1, 2, 3, 5]

a.append([1, 2])
print(a)     # [1, 2, 3, 5, [1, 2]]


# 더하기 연산과 비교!
a += [2, 7]
print(a)     # [1, 2, 3, 5, [1, 2], 2, 7]

# 정렬하기
a = [2, 5, 3]
a.sort()
print(a)   # [2, 3, 5]
a.sort(reverse=True)
print(a)   # [5, 3, 2]

# 요소가 리스트 안에 있는지 알아보기
a = [2, 1, 4, "2", 6]
print(1 in a)      # True
print("1" in a)    # False
print(0 not in a)  # True



#딕셔너리:::

# 딕셔너리는 키(key)와 밸류(value)의 쌍으로 이루어진 자료의 모임입니다. 영한사전에서 영어 단어를 검색하면 한국어 뜻이 나오는 것처럼요!
person = {"name":"Bob", "age": 21}
print(person["name"])


# 딕셔너리를 만드는 데는 여러가지 방법을 쓸 수 있습니다.
a = {"one":1, "two":2}

# 빈 딕셔너리 만들기
a = {}
a = dict()

# 딕셔너리의 요소에는 순서가 없기 때문에 인덱싱을 사용할 수 없어요.
person = {"name":"Bob", "age": 21}
print(person[0])   # 0이라는 key가 없으므로 KeyError 발생!

# 딕셔너리의 값을 업데이트하거나 새로운 쌍의 자료를 넣을 수 있습니다.
person = {"name":"Bob", "age": 21}

person["name"] = "Robert"
print(person)  # {'name': 'Robert', 'age': 21}

person["height"] = 174.8
print(person)  # {'name': 'Robert', 'age': 21, 'height': 174.8}

# ​딕셔너리의 밸류로는 아무 자료형이나 쓸 수 있어요. 다른 딕셔너리를 넣을 수도 있죠!
person = {"name":"Alice", "age": 16, "scores": {"math": 81, "science": 92, "Korean": 84}}
print(person["scores"])             # {'math': 81, 'science': 92, 'Korean': 84}
print(person["scores"]["science"])  # 92

# 딕셔너리 안에 해당 키가 존재하는지 알고 싶을 때는 in을 사용합니다.
person = {"name":"Bob", "age": 21}

print("name" in person)       # True
print("email" in person)      # False
print("phone" not in person)  # True

# 딕셔너리는 리스트와 함께 쓰여 자료를 정리하는 데 쓰일 수 있습니다.
people = [{'name': 'bob', 'age': 20}, {'name': 'carry', 'age': 38}]

# people[0]['name']의 값은? 'bob'
# people[1]['name']의 값은? 'carry'

person = {'name': 'john', 'age': 7}
people.append(person)

# people의 값은? [{'name':'bob','age':20}, {'name':'carry','age':38}, {'name':'john','age':7}]
# people[2]['name']의 값은? 'john'



# Q. 연습문제 - 딕셔너리
# smith의 science 점수를 출력해보세요
people = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]

print(people[2]['score']['science'])