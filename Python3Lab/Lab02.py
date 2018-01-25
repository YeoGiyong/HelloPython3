import random

#18 연봉 계산

salary = int(input("연봉을 입력해주세요(3000)"))
isMarried = input("결혼 여부를 입력해주세요(미혼/결혼)")
tax = 0

if isMarried=='미혼' :
    if salary < 3000 :
        tax = salary * 0.1
    else :
        tax = salary * 0.25

elif isMarried=='결혼' :
    if salary < 6000:
        tax = salary * 0.1
    else :
        tax = salary * 0.25

print("결혼 여부 : %s // 연봉 : %d // 납부세 : %d " % (isMarried,salary,tax))

#19 윤년 계산
year = int(input('윤년여부를 알고 싶은 년도를 입력하세요 '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('%d는 윤년 입니다' % year)
else :
    print('%d는 윤년이 아닙니다' % year)

#20 복권 발행

lotto = str(random.randint(100,999)) #세자리 난수 생성

lucky = input('복권번호를 입력하세요 : ')
match = 0 #일치여부

if (lucky[0] == lotto[0] or
    lucky[0] == lotto[1] or
    lucky[0] == lotto[2]):
    match +=1

if (lucky[1] == lotto[0] or
    lucky[1] == lotto[1] or
    lucky[1] == lotto[2]):
    match +=1

if (lucky[2] == lotto[0] or
    lucky[2] == lotto[1] or
    lucky[2] == lotto[2]):
    match +=1

print("추첨번호 : %s, 내 로또 번호 : %s : 일치 수 : %d" %(lotto,lucky,match))

if match == 3:
    print("1등 당첨 : 백만원!!")
elif match ==2:
    print("2등 당첨 : 만원!!")
elif match == 1:
    print("3등 당첨 : 천원!!")
else :
    print("꽝! 다음기회에")


#21 구구단
#숫자만 입력받기
#문자 - ASCII 코드값 : ord()
#ASCII코드값 - 문자 : chr()
#ASCII - 48, 9: ASCII - 57

dan = input('출력할 단을 입력하세요 : ')
if ord(dan[0]) >= ord('0') and ord(dan[0]) <= ord('9'):
    print('구구단 출력')
else:
    print('입력 오류 - 숫자만 입력하세요!!')

for n in range(1,10) :
    print("%s * %d = %d" % (dan,n,int(dan)*n))


#22 소문자를 대문자로 변환

lower = input('소문자를 입력하세요 : ')
if ord(lower[0]) >= ord('a') and ord(lower[0]) <= ord('z') :
    print(lower.upper())
else:
    print('소문자만 입력 가능!!')

#23 숫자 맞추기
#1~100 사이 난수 생성 후 맞추는 게임
key = random.randint(1,100)

while True:
    lucky = int(input('1-100사이 숫자 입력하세요 : '))
    if key == lucky:
        print("빙고!! 숫자를 맞췄습니다")
        break
    elif key < lucky:
        print('으음.. 숫자가 크네요 :( ')
    else:
        print('으음.. 숫자가 작네요 :( ')








