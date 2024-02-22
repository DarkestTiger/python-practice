import random

class RPSerror(Exception): pass

pick = '가위', '바위', '보'

while True:
    try:
        com = random.choice(pick)
        user = str(input(' 가위! 바위!! 보!!!: '))

        if user not in pick:
            raise RPSerror
        print(f'[You] ====> {user} vs {com} <=== [Computer] ')
        if ((user == '가위' and  com == '보') or
            (user == '바위' and  com == '가위') or
            (user == '보' and  com == '바위')):
            print('이겻어!')
            break
        elif ((user == '가위' and  com == '바위') or
            (user == '바위' and  com == '보') or
            (user == '보' and  com == '가위')):
            print ('졋어!!')
            break
        else:
            print ('비겻어!')
            continue
    except RPSerror:
        print ('장난하냐? 애송이야! 가위 , 바위, 보 중에서만 낼 수 있어!')