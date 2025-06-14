import random

secret_number = random.randint(1, 100)
attempts = 0

print("숫자 맞추기 게임을 시작합니다!")

while True:
    try:
        guess = int(input("1부터 100 사이의 숫자를 입력하세요: "))
        attempts += 1
        diff = guess - secret_number  # 양수면 큼, 음수면 작음

        if diff == 0:
            print(f"정답입니다! {attempts}번 만에 맞췄어요.")
            break
        elif diff < -19:
            print("너무 작다.")
        elif diff < 0:
            print("작다.")
        elif diff > 19:
            print("너무 크다.")
        else:
            print("크다.")
    except ValueError:
        print("숫자를 입력해주세요.")
