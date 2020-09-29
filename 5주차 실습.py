#5주차 실습 1

a = {}

if a:
    	print('참입니다.')
else:
	print('거짓입니다.')

b = 123

if b:
    	print('참입니다.')
else:
	print('거짓입니다.')

#5주차 실습 2

num = int(input())

if (num<=-10 or num>=10):
	print("1점입니다.")
	
elif (num<=-7 or num>=7):
	print("2점입니다.")
	
elif (num<=-3 or num>=3):
	print("3점입니다.")
	
elif (num<=-1 or num>=1):
	print("4점입니다.")
	
elif (num==0):
	print("축하합니다! 5점입니다.")
	
else:
	print("점수를 출력할 수 없습니다.")

#5주차 실습 3

num = int(input())

if(num <= 0):
	print('자연수가 아닙니다.')
	
elif (num % 2 == 1):
	print('입력한 수 %d는 홀수입니다.'%num)
	
else:
	print('입력한 수 %d는 짝수입니다.'%num)


#5주차 마무리 과제

year = int(input())

if(year%4==0 and year%100>0 or year%400==0):
    print('연도를 입력하세요: %d년은 윤년입니다.'%year)
    
else:
    print('연도를 입력하세요: %d년은 윤년이 아닙니다.'%year)
