# 예를 들어 20세 보다 큰 사람만 출력한다고 해보자

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    if person['age'] > 20:
        print (person['name'])

# 그런데 만약, bobby가 age를 갖고 있지 않다면?


people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby'},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    if person['age'] > 20:
        print (person['name'])

# 그 때 아래와 같이 try except 구문을 이용하면 에러를 넘길 수 있다.

for person in people:
    try:
        if person['age'] > 20:
            print (person['name'])
    except:
        name = person['name']
        print(f'{name} - 에러입니다')