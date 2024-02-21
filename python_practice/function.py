def hello():
  print('안녕')
  print('좋은 날씨야')

hello()
hello()

# 함수는 반복적으로 사용하는 코드들에 이름을 붙여놓은 거다.

def sum(a,b):
  return a+b

result = sum(1,2)
print(result)

# 덧셈을 해도 되고

def bus_rate(age):
    if age > 65:
        print("무료로 이용하세요")
    elif age > 20:
        print("성인입니다.")
    else:
        print("청소년입니다")

bus_rate(27)
bus_rate(10)
bus_rate(72)

# 조건문에 넣을 값을 바꿔가면서 결과를 확인할수도 있고

def bus_fee(age):
    if age > 65:
        return 0
    elif age > 20:
        return 1200
    else:
        return 0     


money = bus_fee(28)
print(money)
# 단순한 출력 뿐만 아니라 결과 값을 돌려주도록 함수를 만들 수도 있다.

# 연습문제
# 주민등록번호를 입력받아 성별을 출력하는 함수 만들어보기.
def check_gender(pin):
    num = int(pin.split('-')[1][0])
    if num % 2 == 0:
        print('여성')
    else:
        print('남성')

my_pin = "200101-3012345"
check_gender(my_pin)