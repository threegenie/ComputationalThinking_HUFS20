#12주차 실습 함수의 구성과 사용
def my_func():
	sum=0
	for i in range(5):
		a = int(input())
		sum+=a
		
	return sum

total = my_func()
print(total)

#12주차 마무리 과제
def average(a,b,c):
	return (a+b+c)/3

kor = int(input('국어 점수를 입력하세요: '))
eng = int(input('영어 점수를 입력하세요: '))
math = int(input('수학 점수를 입력하세요: '))

print('국어는 %d점, 영어는 %d점, 수학은 %d점이며, 총 평균은 %.2f점입니다.'%(kor,eng,math,average(kor,eng,math)))
