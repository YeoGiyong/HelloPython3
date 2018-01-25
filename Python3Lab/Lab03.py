# 지금까지의 예제를 함수로 재작성
# Qna8, Qna10, Qna11, Qna12,
# Qna17, Qna18, Qna19, Qna20
import random

#Qna8 생활속 문제를 파이썬으로 풀기(함수로풀기)
print("########## 8 ########### \n")
def compareRoom(width,height,price):
    return (width * height)/price

roomA = compareRoom(2.5,3,27)
roomB = compareRoom(4,2,30)

if(roomA>roomB):
    print('방A가 낫네요')
else:
    print('방B가 낫네요')

#10 이율율 계산 - 도메인 문제(함수로 풀기)
print("########## 10 ########### \n")
def computeProfit():
    c= int(input('불변자본을 입력하세요'))
    v= int(input('가변자본을 입력하세요'))
    s= int(input('잉여가치액을 입력하세요'))

    #constant capital(불변자본) , variable capital(가변자본)
    #surplus value(잉여가치액)
    return (c+v)/s

print(computeProfit())

#11 환율에 따른 노트북 구매(함수)
#달러 환율 : 1071, 2018.01.22 현재
#유로 환율 : 1309, 2018.01.22 현재
print("########## 11 ########### \n")

def getExchangeRate(country):
    rate = 0
    if country == 'us':
        rate = 1071
    elif country == 'euro':
        rate = 1309
    return rate

buyUS = 780 * getExchangeRate('us')
buyEuro = 650 * getExchangeRate('euro')

if buyUS > buyEuro:
    print('유로화를 구입하는게 더 싸네요')
else :
    print('달러로 구입하는게 더 싸네요')

#12 운동장 너비 계산(함수)
print("########## 12 ########### \n")

def howManyRun(radius):
    pi = 3.14
    return radius * pi

studentA = howManyRun(100)
studentB = howManyRun(90)

print('학생A는 학생B보다 %d만큼 더 뜀' % (studentA - studentB))


#17 계산기(제곱연산 추가)
print("########## 17 ########### \n")

def intCalu():
    num1 = int(input('좌변값을 하나 입력하세요'))
    num2 = int(input('우변값을 하나 입력하세요'))
    fmt = "%d + %d = %d \n %d + %d = %d \n"
    fmt += "%d * %d = %d \n %d / %d = %.5f \n"
    fmt += "%d ** %d = %d"
    print(fmt % (num1,num2,num1+num2, \
                 num1,num2,num1-num2, \
                 num1,num2,num1*num2, \
                 num1,num2,num1/num2, \
                 num1,num2,num1**num2))
intCalu()

#18 세금 계산(함수)
print("########## 18 ########### \n")
def computeTax():
    salary = int(input("연봉을 입력해주세요 : "))
    isMarried = input("결혼 여부를 입력해주세요(Y/N) : ")

    if isMarried.upper() == 'N':
        if salary < 3000:
            tax = salary * 0.1
        else:
            tax = salary * 0.25
        isMarried = "아니오"

    else:
        if salary < 6000:
            tax = salary * 0.1
        else:
            tax = salary * 0.25
        isMarried = "예"

    fmt = "연봉 : %d, 결혼여부 : %s, 세금 : %.1f"
    print(fmt % (salary,isMarried,tax))

computeTax()

#19 윤년 계산(함수)
print("########## 19 ########### \n")
def isLeapYear():
    year = int(input('윤년여부를 알고 싶은 년도를 입력하세요 : '))
    isleap = '윤년입니다'

    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        isleap = '윤년입니다'

    print("%d는 %s" %(year,isleap))

isLeapYear()

#20 복권발행
print("########## 20 ########### \n")
def rouletteLotto():
    lotto = str(random.randint(100,999)) #세자리 난수 생성
    lucky = input('복권번호를 입력하세요 : ')
    match = 0 #일치여부
    prize ="꽝! 다음기회에!"

    for i in [0,1,2]:
        for j in [0,1,2]:
            if (lucky[i] == lotto[j]):
                match +=1

    if match == 3:
        prize = '1등 당첨! 상금 백만원'
    elif match == 2:
        prize = '2등 당첨! 상금 만원'
    elif match == 1:
        prize = '3등 당첨! 상금 천원'

    print(lucky,lotto,prize)

rouletteLotto()