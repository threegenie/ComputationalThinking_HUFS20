#13주차 실습 매개변수
def calNums(base,*nums):
	for i in nums:
		total = 1
		for j in range(0,i):
			total*=base
		print(f'{base}의 {i} 제곱 값은 {total}이다.')
		
calNums(5, 1, 2, 3)
calNums(2, 2, 4, 6, 8, 10)

#13주차 실습 반환값
def my_func(x):
	a = x.upper()
	b = x.lower()
	return (a,b)
	
string = input()
print(my_func(string))

#13주차 전역변수와 지역변수
def maxFunc(A):
	max = 0
	for i in range(len(A)) :
		if max<A[i]:
			max=A[i]
		
	return max

A = [1, 2, 3, 4, 5, 6, 73, 8, 10, 54] 
maxNum = maxFunc(A)
print(maxNum)

#13주차 마무리 과제
a = int(input('투자 액수를 입력하세요: '))
b = int(input('투자한 날짜 수를 입력하세요: '))

total = 10000
total = a

if a>=100 and a<=10000 and b>=1 and b<=10:
	for i in range(1,b+1):
		change = int(input('%d일차 변동 데이터를 입력하세요: '%i))
		for j in range(i, i+1):
			total += total*(change/100)

ben = total - a
print('%d'%ben)

if ben>0:
	print('이득입니다.')
elif ben == 0:
	print('본전입니다.')
else:
	print('손해입니다.')
