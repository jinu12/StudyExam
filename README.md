# backjoonSolve

backjoon solve remove https://github.com/jinu12/backjoon

# 로또 프로그램

```python
import random
import time

def menustr():

    print("=" * 70)
    print(" " * 30 + "로또시작" + " " * 30)
    print("=" * 70)

    answwer = "수동으로 하시겠습니까? 자동으로 하시겠습니까?"
    exam = "1.자동 2.수동 3.종료\n"
    inputtext = "입력 : "

    print(answwer + exam + inputtext, end='')

def lottoStartStr():

    time.sleep(3)
    print("=" * 70)
    print("로또 구매 시간이 지났습니다.")
    print("담청자를 조회합니다.")
    print("=" * 70)

def lottoprocess(lotto_nums, user_nums):

    totalmoeny = '총 담첨 금액 : '
    selectmoney = '담첨 금액 : '
    bonus = lotto_nums[6]
    money = random.choice(range(1000000000, 10000000000))

    print(totalmoeny + format(int(money), ','))
    print("=" * 70)

    collect_num = []  # 맞춘 리스트 초기화

    count = 0  # 맞은 갯수 초기화

    for n in range(0, 6):  # count 변수를 통해 구매번호와 당첨번호 리스트 내부의 변수가 같은지 판별하여, 같으면 count 숫자를 하나씩 올린다.
        for k in range(0, 6):
            if lotto_nums[n] == user_nums[k]:
                collect_num.append(lotto_nums[n])
                count = count + 1

    if count == 6:
        print("1등 담첨이 되었습니다.")
        print(selectmoney + str(money * 0.5))

    elif count == 5:  # 5개가 같고, 보너스 숫자가 들어 있다면 2등
        if user_nums.count(bonus) == 1:
            print("맞은 숫자는 {} 맞춘 갯수 {}개, 보너스 숫자는 {} 2등에 담청되었습니다..".format(sorted(collect_num), count, bonus[0]))
            print(selectmoney + str(money * 0.3))
        else:
            print("맞은 숫자는 {} 맞춘 갯수 {}개, 보너스 숫자는 {} 3등에 담청되었습니다..".format(sorted(collect_num), count, bonus[0]))
            print(selectmoney + str(money * 0.1))

    elif count == 4:
        print("맞은 숫자는 {} 맞춘 갯수 {}개, 4등에 담청되었습니다".format(sorted(collect_num), count))
        print(selectmoney + str(money * 0.005))

    elif count == 3:
        print("맞은 숫자는 {} 맞춘 갯수 {}개, 5등에 담청되었습니다..".format(sorted(collect_num), count))
        print(selectmoney + str(money * 0.0000001))

    else:
        if count == 0:
            print("맞은 숫자는 횟수가 없어서 담첨 되지 않았습니다.")
            print(selectmoney + "0")
        else:
            print("맞춘 갯수 {}개, 담첨 되지 않았습니다.".format(count))
            print(selectmoney + "0")

def lottoProgram():  # 로또 프로그램 함수 정의
    while True:  # 필요 모듛 불러오기

        menustr()
        select = int(input())

        user_num = []  # 로또 구매자의 리스트 초기화

        if select == 1:
            print("로또 자동으로 구매합니다.")
            user_num = random.sample(range(1, 46), 6)
            print("사용자 구매 번호", sorted(user_num))

        elif select == 2:  # 입력 시, random함수를 통해 6자리 숫자 추출하기
            print("로또 수동으로 구매합니다.")
            for i in range(0, 6):
                user_num.append(int(input("{} 숫자 : ".format(i+1))))
            print("사용자 구매 번호", sorted(user_num))

        elif select == 3:
            print("로또를 종료합니다.")
            break

        else:
            print("정확한 숫자를 입력해주세요.")

        lottoStartStr()

        lotto_num = random.sample(range(1, 46), 7)  # random함수를 통해 당첨번호 7개의 숫자 추출하기
        bonus = [lotto_num[6]]  # 보너스 번호는 lotto_num의 마지막 번호를 받아오기

        print("로또 번호", sorted(lotto_num[:6]))
        print("보너스 로또 번호 : ", bonus[0])

        lottoprocess(lotto_num, user_num)

def start():
    lottoProgram()

if __name__ == '__main__':
    start()
```
