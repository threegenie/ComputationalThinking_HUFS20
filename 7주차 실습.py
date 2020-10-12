#7주차 중첩 반복문 이론 문제

for x in range(0, 101, 1):
    for y in range(50, 76, 2):
        print("(%d, %d)" %(x, y))


#7주차 실습 1

num = int(input())

for i in range(1,num+1) :
	for j in range(num-i):
		print(' ',end='')
	
	for k in range(i):
		print('*',end='')

	print()


'''
num에 줄 수 입력받음
range 함수에서 끝 값은 포함이 안되므로 줄 반복 범위는 1부터 num+1까지
첫번째 j가 있는 for문에서 '전체줄수-i'만큼 공백을 출력한다
두번째 j가 있는 for문에서 줄 수만큼 별을 출력한다.
'''

#7주차 실습 2

drink = 3
while True:

    money = int(input("돈을 넣어 주세요: "))

    if money == 300:
	print("음료 나왔습니다.")
	drink -= 1

    elif money > 300:
    	print("거스름돈 %d원과 음료 나왔습니다." %(money-300))
	drink -= 1

    elif money < 300:
        print("잔액이 부족합니다.\n남은 음료 갯수는 %d개 입니다." %(drink))

    if drink<=0:
        money = int(input("돈을 넣어 주세요: "))
	print("음료가 다 떨어져서 영업이 종료되었습니다.")
	break

#7주차 마무리 과제

while True:
	print("1. 더하기")
	print("2. 빼기")
	print("3. 곱하기")
	print("4. 나누기")
	print("5. 프로그램 종료")
	menu = int(input("원하는 기능의 번호를 입력하세요: "))

	if menu == 5:
		print("프로그램을 종료합니다.")
		break
	
	elif menu > 5 or menu < 1:
		print("잘못된 번호입니다.")
        
	else:
		one=int(input("첫 번째 정수를 입력하세요: "))
		two=int(input("두 번째 정수를 입력하세요: "))

		if menu == 1:
			print("%d와 %d를 더하기 연산한 결과는 %d입니다." %(one, two, one+two))
		elif menu == 2:
			print("%d에서 %d를 빼기 연산한 결과는 %d입니다." %(one, two, one-two))
		elif menu == 3:
			print("%d와 %d를 곱하기 연산한 결과는 %d입니다." %(one, two, one*two))
		elif menu == 4:
			if two != 0:
				print("%d를 %d로 나누기 연산한 결과는 %.6f입니다." %(one, two, one/two))
			else:
				print("연산이 불가합니다.")
        
	
#7주차 어문계열

plot = """\'플롯(plot)\'이란 어떤 일련의 사건들을 예술적으로 정리한 것을 일컫거나
극, 소설, 시 등의 계획 또는 설계, 줄거리를 의미합니다.
좀 더 자세히 설명하자면 플롯은 문학작품의 액션 구조라고 할 수 있는데,
이 액션들은 작품 속 등장인물들에 의해 행해지며, 그들의 자질을 표현하는 수단이 됩니다.

1. Protagonist: 여러 등장인물 또는 성격 중 가장 주요한 성격으로, 단순하게 표현하면 \'주인공\'입니다.
2. Antagonist: Protagonist에 대항하는 상대 성격입니다.
3. Hero: Protagonist를 의미하는 경우가 많지만 종종 \'용기\', \'영광\', \'숭고함\' 등을 표현합니다."""

finder = True

while finder:
	keyword = input("존재하는지 알고 싶은 키워드를 검색하세요(검색을 끝내고 싶다면 out을 입력하세요): ")
	
	if keyword == "out":
		finder = False
	elif plot.find(keyword)==-1:
		add_content = input("해당 키워드에 대한 설명을 추가 작성해주세요: ")
		plot = plot + '\n' + add_content
		print(plot)
	else:
		print("%s는 앞에서부터 %d번째 위치에 있습니다." %(keyword, plot.find(keyword)+1))


#7주차 상경계열
calc = True

PV = 1000
year = 5

while calc:
	base = 1
	k = int(input('수익률을 % 단위로 입력하세요. 종료를 원하시면 음수를 입력합니다: '))
	
	if k<0:
		print('종료합니다.')
		calc = False
	else:
		for i in range(year):
			base *= (1+k/100)
		FV = PV * base
		print('원금이 %d원이고 연 수익률이 %d%%일 때 %d년 후 미래가치는 %.2f원입니다.' %(PV,k,year,FV))
		
		
#7주차 자연계열
calc = True

while calc:
	fib1 = 1
	fib2 = 1
	tmp = 0
	num = int(input('3 이상의 정수를 입력합니다. 3 미만의 수를 입력하면 종료됩니다: '))
	
	if num < 3:
		print('종료합니다.')
		calc = False
	else : 
		for i in range(1, num+1):
			if i == 1:
				print('{0}번 피보나치 수는 {1}입니다.'.format(i,fib1))
			elif i == 2:
				print('{0}번 피보나치 수는 {1}입니다.'.format(i,fib2))
			else:
				print('{0}번 피보나치 수는 {1}입니다.'.format(i,fib1+fib2))
				tmp = fib2
				fib2 = fib1+tmp
				fib1 = tmp
