#11주차 실습 튜플 자료형 

T1 = ('a','b','c')
T2 = (1,2,3)
T3 = (4,'d')

print(T1[2],T2[1])

T1 = T1 + T3
print(T1)

print(T1[2:5])
print(T3*T2[2])


#11주차 실습 집합 자료형

S1 = {1, 3}
S2 = {2, 3}
num_list = [1, 3, 4, 5]

print(S1.intersection(S2))
print(S1.difference(S2))

S1.add('hufs')
S1.update(num_list)
print(S1)

#11주차 마무리 과제
d = {'pencil':'500','eraser':'700','notebook':'1500','eraser':'700','scissors':'3000','tape':'2700','pencil':'500','pencil':'500','notebook':'1500','tape':'2700'}

d['white']='1900'
print(d.get('white'))

num = d.keys()
print(len(num))

#11주차 계열별 예제 - 어문계열


finder = True
history = []
index = -1

while finder:
	what = input('어떤 작업을 진행하시겠습니까? 끝내길 원하신다면 \'종료\'를 입력하세요: ')
	
	if what == '종료':
		print('종료합니다')
		finder = False
	elif what == '기록':
		time=input('시기: ')
		data1=input('문학적 경향: ')
		data2=input('대표 작가: ')
		data3=input('소설명: ')
		
		history.append([time,data1,data2,data3])
		index+=1
		print(history)
		
	elif what == '추출':
		if index<0:
			print('정보가 없습니다')
		else:
			print(f'{history[0][0]}의 문학적 경향은 {history[0][1]}입니다. 이 시기 대표 작가 {history[0][2]}은(는) {history[0][3]} 소설을 집필했습니다.')
			history.remove(history[0])
			index -= 1
	
	else:
		print('잘못된 입력입니다')

#11주차 계열별 예제 - 상경계열

finder = True
company = []
index = -1

while finder:
	what = input('어떤 작업을 진행하시겠습니까? 끝내길 원하신다면 \'종료\'를 입력하세요: ')
	
	if what == '종료':
		print('종료합니다')
		finder = False
	elif what == '입력':
		name=input('자회사 이름: ')
		data1=input('유동자산: ')
		data2=input('재고자산: ')
		data3=input('유동부채: ')
		
		company.append([name,data1,data2,data3])
		index+=1
		print(company)
		
	elif what == '추출':
		if index<0:
			print('정보가 없습니다')
		else:
			print(f'{company[0][0]} 자회사의 유동자산은 {company[0][1]}만원, 재고자산은 {company[0][2]}만원, 유동부채는 {company[0][3]}만원입니다.')
			company.remove(company[0])
			index -= 1
	
	else:
		print('잘못된 입력입니다')
		
		
#11주차 계열별 예제 - 자연계열
		

finder = True
experiment = []
index = -1

while finder:
	what = input('어떤 작업을 진행하시겠습니까? 끝내길 원하신다면 \'종료\'를 입력하세요: ')
	
	if what == '종료':
		print('종료합니다')
		finder = False
	elif what == '기록':
		data1=input('시약 영문: ')
		data2=input('시약 국문: ')
		data3=input('시약 용량: ')
		
		index+=1
		experiment.append([index+1,data1,data2,data3])
		#index+=1
		print(experiment)
		
	elif what == '추출':
		if index<0:
			print('정보가 없습니다')
		else:
			print(f'{experiment[0][0]}번 순서에서 사용된 시약은 {experiment[0][1]}({experiment[0][2]}) {experiment[0][3]}입니다.')
			experiment.remove(experiment[0])
			index -= 1
	
	else:
		print('잘못된 입력입니다')
		
		
