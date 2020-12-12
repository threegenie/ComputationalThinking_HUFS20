#12주차 마무리 과제
def average(a,b,c):
	return (a+b+c)/3

kor = int(input('국어 점수를 입력하세요: '))
eng = int(input('영어 점수를 입력하세요: '))
math = int(input('수학 점수를 입력하세요: '))

print('국어는 %d점, 영어는 %d점, 수학은 %d점이며, 총 평균은 %.2f점입니다.'%(kor,eng,math,average(kor,eng,math)))
