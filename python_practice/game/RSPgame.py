import random


sissor = '가위'

rock = '바위'

paper = '보'


Rules = [sissor, rock, paper]

computer = random.randint(0,2)

user = int(input('| 가위 : 0, 바위 : 1, 보! : 2 | '))

print("나의 선택 :  ")
print(Rules[user])

print("컴퓨터의 선택 :  ")
print(Rules[computer])

if computer == user :
    print('비겼네요?')
elif user - computer == -1 or (user == 2 and computer == 0) :
    print('이겼습니다!')
else:
    print('졋습니다....ㅠㅠ')
        