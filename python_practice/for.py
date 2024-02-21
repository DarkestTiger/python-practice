fruits = ['사과','배','감','수박','딸기']

for fruit in fruits:
  print(fruit)
# 이렇게 했을때 변수 fruits안에 있는 리스트를 돌면서 반복적으로 fruit에 값을 꺼내서 반환한다.
#쉽게 말해 오른쪽 변수의 값을 왼쪽에 반복적으로 넣어주는거다.
  
# 자, 그렇다면 이번엔 사람들이 있다.
  
  people = [
    {'name':'bob','age':'20'},
    {'name':'carry','age':'38'},
    {'name':'john','age':'7'},
    {'name':'smith','age':'17'},
    {'name':'ben','age':'27'},
    {'name':'bobby','age':'57'},
    {'name':'red','age':'32'},
    {'name':'Queen','age':'25'}
  ]

# 사람들은 리스트-딕셔너리 형태로 저장되어있다.
  
# 여기에 예를들어 for person in people 하면 각각의 사람들을 person에 뽑아서 출력할거다.
# 이때 for옆에 있는, 왼쪽의 변수 이름은 아무렇게나 지정해도 사용할수있다.
  #출력 결과 : {'name':'bob','age':'20'}
  #     {'name':'carry','age':'38'}
    #   {'name':'john','age':'7'}
    #   {'name':'smith','age':'17'}
    #   {'name':'ben','age':'27'}
    #   {'name':'bobby','age':'57'}
    #   {'name':'red','age':'32'}
    #   {'name':'Queen','age':'25'}
  
# 자 그러면 우리가 여기서 이름과 나이만 각각 뽑고싶다면 어떻게 해야 할까?
  # 아래의 코드를 보자!

  for person in people:
    name = person['name']
    age = person['age']
    print(name, age)

#  이렇게 하면 이름과 나이만 각각 뽑힌다.
  # bob 20
  # carry 38
  # john 7
  # smith 17
  # ben 27
  # bobby 57
  # red 32
  # Queen 25
    
# 만약 이들중에 성인인 사람만 뽑고 싶다면??
for person in people:
  name = person['name']
  age = person['age']
  if age > 20:
    print(name, age)

# 이렇게 나이가 20보다 큰사람만 출력하게 해서 성인인 사람만 뽑아낼수도 있다.

#만약 반복문을 돌면서 이 사람들 각각에게 순번을 나눠주어 줄세우려면 어떻게 해야할까?

for i, person in enumerate(people):
      name = person['name']
      age = person['age']
      print(i, name, age)

#이렇게 하면 된다.
    
    #  그런데 만약, 반복문이 돌면서 순번을 정해주는데, 일정 번호에서 멈춰주고싶을땐 이렇게 해보자.


for i, person in enumerate(people):
      name = person['name']
      age = person['age']
      print(i, name, age)
      if i > 5:
        break
    
    # 이렇게 break문을 사용하면 멈춰줄수있다.


#  연습문제 1
      # 짝수 출력하기
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

for num in num_list:
   if num % 2 == 0:
      print (num)

# 연습문제 2
      # 리스트에서 짝수의 갯수 출력하기
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

count = 0

for num in num_list:
    if num % 2 == 0:
        count += 1

print(count)