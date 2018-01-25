import random


#17 계산기 (제곱연산 추가)
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

#19 윤년여부
def isLeapYear():
    year = int(input('윤년여부를 알고 싶은 년도를 입력하세요 : '))
    isleap = '윤년입니다'

    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        isleap = '윤년입니다'

    print("%d는 %s" %(year,isleap))

#20 복권발행
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

#성적 데이터 클래스
class SungJukVO:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

#성적 처리용 클래스
class SungJukService:
    def getTotal(self,sj1):
        tot = sj1.kor + sj1.eng + sj1.mat
        return tot

    def getAverage(self,sj1):
        avg = self.getTotal(sj1)/3
        return avg

    def getGrade(self,sj1):
        grdlist = '가가가가가가미양우수수'
        var = int(self.getAverage(sj1)/10)
        grd = grdlist[var]
        return grd

