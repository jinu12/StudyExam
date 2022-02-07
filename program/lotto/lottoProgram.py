# 파이썬 로또 프로그램 짜기

"""
프로그램 흐름 정의
1. 로또 넘버를 6개 받는다.
    1-1. 자동 또는 수동으로 구분
    1-2. 자동일 경우 random함수로 숫자를 받아 리스트를 만든다.
    1-2. 수동일 경우 1부터 45까지 6자리 숫자를 입력받아 리스트를 만든다.

2. 로또 당첨 번호를 7개 받는다.
    2-1. random 함수를 통해 1부터 45까지 7개의 숫자를 뽑는다.
    2-2. 뽑은 7개의 숫자 중 로또 당첨 번호 6자리와 보너스 1자리를 각각 리스트에 저장한다.

3. 비교하여 등수를 매기고 출력한다.
    3-1. 각 리스트를 비교하여 동일한 값이 있으면 맞춘 횟수가 올라가게 만든다.
    3-2. 6개는 1등, 5개 + 보너스1개는 2등, 5개는 3등, 4개는 4등, 3개는 5등으로 나눈다.
"""
# 필요 모듈 불러오기
import random


def lottoProgram():  # 로또 프로그램 함수 정의
    while True:  # 필요 모듛 불러오기
        count = 0
        user_num = []  # 로또 구매자의 리스트 초기화
        collect_num = []  # 맞춘 리스트 초기화
        select = int(input("수동으로 하시겠습니까? 자동으로 하시겠습니까? 1: 자동, 2: 수동 3: 종료"))
        if select == 1:  # 1 입력 시, random함수를 통해 6자리 숫자 추출하기
            print("로또 자동으로 구매합니다.")
            user_num = random.sample(range(1, 46), 6)
            print("사용자 구매 번호", sorted(user_num))
        elif select == 2:
            print("로또 수동으로 구매합니다.")
            for i in range(0, 6):
                user_num.append(int(input("{} 숫자 : ".format(i+1))))
            print("사용자 구매 번호", sorted(user_num))
        elif select == 3:
            print("로또를 종료합니다.")
            break
        else:
            print("정확한 숫자를 입력해주세요.")
        print("로또 구매 시간이 지났습니다.")
        print("담청자를 조회합니다.")
        lotto_num = random.sample(range(1, 46), 7)  # random함수를 통해 당첨번호 7개의 숫자 추출하기
        bonus = [lotto_num[6]]  # 보너스 번호는 lotto_num의 마지막 번호를 받아오기
        print("로또 번호", sorted(lotto_num[:6]))
        print("보너스 로또 번호 : ", bonus[0])
        for n in range(0, 6):  # count 변수를 통해 구매번호와 당첨번호 리스트 내부의 변수가 같은지 판별하여, 같으면 count 숫자를 하나씩 올린다.
            for k in range(0, 6):
                if lotto_num[n] == user_num[k]:
                    collect_num.append(lotto_num[n])
                    count = count + 1
        if count == 6:
            print("1등 담첨이 되었습니다.")
            break
        elif count == 5:  # 5개가 같고, 보너스 숫자가 들어 있다면 2등
            if user_num.count(bonus[0]) == 1:
                print("맞은 숫자는 {} 같은 담첨 숫자는 {} 보너스 숫자는 {} 2등에 담청되었습니다..".format(sorted(collect_num), count, bonus[0]))
            else:
                print("맞은 숫자는 {} 같은 담첨 숫자는 {} 보너스 숫자는 {} 3등에 담청되었습니다..".format(sorted(collect_num), count, bonus[0]))
        elif count == 4:
            print("맞은 숫자는 {} 같은 담첨 숫자는 {}개, 4등에 담청되었습니다".format(sorted(collect_num), count))
        elif count == 3:
            print("맞은 숫자는 {} 같은 담첨 숫자는 {}개, 5등에 담청되었습니다..".format(sorted(collect_num), count))
        else:
            if count == 0:
                print("맞은 숫자는 횟수가 없어서 담첨 되지 않았습니다.".format(sorted(collect_num), count))
            else:
                print("맞은 숫자는 {} 같은 담첨 숫자는 {}개, 담첨 되지 않았습니다.".format(sorted(collect_num), count))


lottoProgram()

