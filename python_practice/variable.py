a = 3
b = 2

#변수 만드는 방법
#변수이름 = 값, 문자열

print(a+b)
#덧셈
print(a-b)
#뺄셈
print(a*b)
#곱셈
print(a/b)
#나눗셈
print(a**b)
#제곱 (a의 b제곱)
print(a%b)
#a나누기 b의 나머지


sosu = 11.5
print(sosu)
#변수에는 소수형 데이터도 넣을수 있고

name = 'junseung'
print(name)
#문자형 데이터도 넣을수 있어요.

cham = True
lie = False
print(cham)
print(lie)
# 변수에는 참인지 거짓인지를 판별하는 불리언데이터도 들어갈수있어요.

same = (a == b)
print(same)
# ==도  =처럼 같다 라는 의미를 가집니다.
# 그러나 =와 ==의 차이는 분명하게 존재합니다.
# = 의 경우는 오른쪽의 값을 왼쪽에 대입한다는 의미입니다.
#예를들어  a = 3일경우 3을 변수 a에 대입하는 겁니다.

#그러면 ==의 의미는 뭘까요??
# ==은 두 값이 같은지 비교하여 불리언으로 반환하는겁니다.
#예를들어 a = 3이고 b = 2일 경우 c = (a==b)일때, a와 b의 값이 서로 다르므로 False가 출력됩니다.
#만약에 a와 b모두 3일경우 c = (a==b) 라면, 두 값이 모두 같으므로 True가 됩니다.

# =====================================================================================================
#자, 여기는 강의에 없는 심화 부분

#변수에는 전역변수와 지역변수가 있습니다.

#예를 들어

a = 3

b = 2

#이것은 전역변수 입니다.
#함수 혹은 블록밖에서 선언되었기 때문이죠.
#전역변수는 함수나 블록뿐만  아니라 코드 전반에 있어서 전역적으로 사용될수있습니다.
#즉, 재활용이 가능하다는 말입니다

def variable():
  a = 2

  b = 3
  return print (a,b)

#자 이것은 함수구요, 변수였던 a 와 b는 이미 밖에서 한번 사용되었습니다만
#전역 변수 a,b 와 이것은 다른 변수입니다.
# 파이썬에서 블록문은 들여쓰기를 기준으로 블록으로 인식하는데요
# 대표적으로 조건문 같은것에서 사용될 수 있습니다, 이때 들여쓰기 수준이 같으면 같은 블록에 위치하게 되는거에요.
#이렇게 함수나 블록 안에서 선언된 변수를 지역변수라고 하며 이것은 자기자신이 쓰여진 지역 안에서만 사용되는 변수에요
#그래서 지역변수라고 한답니다.

#자, 그러면 지역변수와 전역변수중에 누가 먼저 실행될까요?
# 두 변수중의 우선순위는 전역변수가 지역변수보다 우위에 있어 먼저 실행된답니다.
# 전역변수 > 지역변수
a