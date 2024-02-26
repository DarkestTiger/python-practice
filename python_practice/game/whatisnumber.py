import random

# class ValueError(Exception):pass

def updown_game():
    random_number = random.randint(1, 100)
    count = 0

    print("업다운 게임을 시작합니다. 1부터 100까지의 숫자 중 하나를 생각하겠습니다.")

    while True:
        try:
            num = int(input("숫자를 추측해보세요: "))
            count += 1

            if num < random_number:
                print("업(Up)")
            elif num > random_number:
                print("다운(Down)")
            else:
                print(f"축하합니다! 숫자를 맞췄습니다. 정답은 {random_number}입니다.")
                print(f"시도한 횟수: {count}")
                break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
        
updown_game()