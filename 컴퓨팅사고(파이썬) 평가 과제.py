# 컴퓨팅사고(파이썬) 평가 과제 - 김재빈 교수님 수업
# 12월 8일까지 제출이라 제출기간이 끝난 후에 업로드할 예정
'''
사용자의 입력(0~3)을 통해 아래의 메뉴를 무한 반복 실행하는 프로그램을 구현하시오.
§1번 가위바위보 게임 : 두 개의 랜덤한 값을 만들어서 모두 10번을 가위바위보 게임을 수행하고 실행화면과 같이 결과를 표시함
§2번  최대공약수 구하기 : 두 개의 수를 랜덤한 값(1~100)으로 만들어서 모두 10번을 최대공약수를 구하고 실행화면과 같이 결과를 표시함
§3번 성적평가 프로그램 : 랜덤한 값(0~100)을 생성하여 리스트에 저장하고 90점이상(A), 80점이상(B), 70점이상(C), 60점이상(D), 그외는  (F)로 평가하여 결과값도 리스트에 저장하고 실행화면과 같이 모두 10번의 결과를 표시함
§0번 종료합니다. : 0번인 경우에 무한 루프를 종료하며 제출자의 (학과/학년/학번/이름) 내용을 화면에 표시함
§0~3번 이외의 번호 : ‘올바른 메뉴 선택이 아닙니다.’ 를 화면에 표시하고 계속해서 작업할 메뉴를 입력 받기 위한 동작을 하여야 함
§위의 0,1,2,3 번각각의 동작을 함수를 사용하여 구현하시오
'''

import random
from math import gcd

def one():
	print("\n[1] 가위(0), 바위(1), 보(2) 게임")
	print("==============================")
	for i in range(10):
		a = random.randint(0,2)
		b = random.randint(0,2)
		i += 1
		if(a==b):
			print("%d) user1 : %d user2 : %d user1 = user2"%(i,a,b))
		elif(a>b):
			print("%d) user1 : %d user2 : %d user1 > user2"%(i,a,b))
		elif(a<b):
			print("%d) user1 : %d user2 : %d user1 < user2"%(i,a,b))
		
def two():
	print("\n[2] 최대 공약수를 구해 봅시다")
	print("==============================")
	
	for i in range(10):
		a = random.randint(1,100)
		b = random.randint(1,100)
		i += 1
		div = gcd(a,b)
	
		print("%d) 두개의 정수 (%d, %d) 최대 공약수는 %d"%(i,a,b,div))
	

def three():
	print("\n[3] 성적을 평가하여 봅시다")
	print("==============================")
	
	for i in range(10):
		a = random.randint(0,100)
		i += 1
		grade = []
		grade.append(a)
		
		if a>=90:
			grade.append('A')
			print("%d)점수 %d 는 학점이 A 입니다."%(i,a))
		elif a>=80:
			grade.append('B')
			print("%d)점수 %d 는 학점이 B 입니다."%(i,a))
		elif a>=70:
			grade.append('C')
			print("%d)점수 %d 는 학점이 C 입니다."%(i,a))
		elif a>=60:
			grade.append('D')
			print("%d)점수 %d 는 학점이 D 입니다."%(i,a))
		else:
			grade.append('F')
			print("%d)점수 %d 는 학점이 F 입니다."%(i,a))
	

print("프로세스가 시작되었습니다.(입력값을 직접 입력해 주세요)\n>")

while True:
	print("\n1 : 가위바위보\n2 : 최대공약수\n3 : 성적평가\n0 : 종료\n")
	user_input = int(input("메뉴에서 선택하세요 : "))
	
	if user_input == 0:
		print("\n컴퓨팅사고(파이썬) 평가과제 제출합니다")
		print("================================")
		print("학과 : 영미권통상통번역전공\n학년 : 4학년\n학번 : 201600535\n이름 : 김세진")
		break
	
	elif user_input == 1:
		one()
	
	elif user_input == 2:
		two()
	
	elif user_input == 3:
		three()
	
	else:
		print("\n올바른 메뉴 선택이 아닙니다.")
	
