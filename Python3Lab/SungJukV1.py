# 성적 처리프로그램 V1
# 이름name, 국어kor, 영어eng, 수학mat
# 총점tot, 평균avg, 학점grd


print('-----성적 처리 프로그램 V1-----')
name = input('이름을 입력하세요 : ')
kor = int(input('국어점수를 입력하세요: '))
eng = int(input('영어점수를 입력하세요: '))
mat = int(input('수학점수를 입력하세요: '))

tot = kor + eng + mat
avg = tot / 3
grd = '가'

if avg >=90:
    grd = '수'
elif avg >=80 :
    grd ='우'
elif avg >=70 :
    grd = '미'
elif avg >=60 :
    grd = '양'

print("이름 : %s // 총점 : %d // 평균 : %.2f // 학점 : %s" % (name,tot,avg,grd))
