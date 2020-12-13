#15주차 실습 모듈이란
import math 

def LCM(data1, data2):
	return (data1*data2)//math.gcd(data1,data2)
	
a = int(input('첫 번째 자연수를 입력합니다: '))
b = int(input('두 번째 자연수를 입력합니다: '))

print(float(LCM(a,b)))

#15주차 계열별 예제 - 어문계열
def del_sign(origin):
	data = origin.replace('.',' ')
	data = data.replace(',',' ')
	data = data.replace('-',' ')
	data = data.replace('"',' ')
	data = data.replace("'",' ')
	data = data.replace('\ufeff',' ')
	data = data.replace('\n',' ')
	ver1 = data.split(' ')
	return ver1

def find_standard(origin):
	set_temp = set(origin)
	set_temp.remove('')
	standard = list(set_temp)
	print('사용된 단어 개수는 총 %d개입니다.'%len(standard))
	return standard

def analysis(origin,standard):
	for i in standard:
		count = 0
		for j in origin:
			if i==j:
				count+=1
		print('%15s=%5d번'%(i,count))

f = open('data/Rapunzel.txt','r')
all = f.read()
f.close()

rapunzel = del_sign(all)
new_standard = find_standard(rapunzel)
result = analysis(rapunzel, new_standard)

#15주차 계열별 예제 - 상경계열

def del_sign(origin):
	data = origin.replace('.',' ')
	data = data.replace(',',' ')
	data = data.replace('-',' ')
	data = data.replace('"',' ')
	data = data.replace("'",' ')
	data = data.replace('\n',' ')
	data = data.replace('(',' ')
	data = data.replace(')',' ')
	data = data.replace('\ufeff',' ')
	temp = data.split(' ')
	return temp

def find_standard(split_list):
	set_temp = set(split_list)
	set_temp.remove('')
	standard = list(set_temp)
	print('사용된 단어 개수는 총 %d개입니다.'%len(standard))
	return standard

def analysis(split_list,standard):
	for i in standard:
		count = 0
		for j in split_list:
			if i==j:
				count+=1
		print('%15s=%5d번'%(i,count))

f = open('data/labour_force_survey.txt','r')
all_data = f.read()
f.close()

ver1 = del_sign(all_data)
new_standard = find_standard(ver1)
analysis(ver1, new_standard)

#15주차 계열별 예제 - 자연계열

def del_sign(origin):
	data = origin.replace('.',' ')
	data = data.replace(',',' ')
	data = data.replace('-',' ')
	data = data.replace('"',' ')
	data = data.replace("'",' ')
	data = data.replace('\n',' ')
	data = data.replace('(',' ')
	data = data.replace(')',' ')
	data = data.replace('\ufeff',' ')
	temp = data.split(' ')
	return temp

def find_standard(split_list):
	set_temp = set(split_list)
	set_temp.remove('')
	standard = list(set_temp)
	print('사용된 단어 개수는 총 %d개입니다.'%len(standard))
	return standard

def analysis(split_list,standard):
	for i in standard:
		count = 0
		for j in split_list:
			if i==j:
				count+=1
		print('%15s=%5d번'%(i,count))

f = open('data/dark_energy.txt','r')
all_data = f.read()
f.close()

ver1 = del_sign(all_data)
new_standard = find_standard(split)
analysis(split, new_standard)



#15주차 마무리 과제
movies = ["Dark Knight", "Harry Porter", "Parasite", "Matrix", "La La Land"]

print()
print("===========영화 목록===========")
for i in movies:
	print(i)
print("==============================")
	
choice = input("예매하실 영화를 선택해주세요: ")

while choice not in movies:
	print("예매할 수 없는 영화입니다")
	choice = input("예매하실 영화를 선택해주세요: ")

print('%s를 선택하셨습니다'%choice)
	
check = False

while(not(check)):
	people = int(input('관람 인원 수를 입력해주세요: '))
	if people <= 0:
		print("관람 인원 수는 양수만 가능합니다")		
	else:
		ckeck = True
		break
print("관람할 인원 수는 %d명입니다" %people)
	
coupon_dic = {'WELCOME':2000, 'VALENTINE':3000, 'CHRISTMAS':4000, 'INDEPENDENCE':5000}
process = True

usage = str(input('할인권을 사용하시려면 y, 금액 확인으로 넘어가시려면 n을 입력해주세요: '))

while process:
	if usage == 'y':
		coupon = input('쿠폰 번호를 입력해주세요: ')
		if coupon in coupon_dic:
			sale = coupon_dic.get(coupon)
			print("%d원 할인됩니다"%sale)
			del(coupon_dic[coupon])
			process = False
		else:
			print('존재하지 않는 할인권입니다')
			usage = input('할인권을 다시 입력하려면 y, 아니면 n을 입력해주세요: ')
	elif usage == 'n':
		sale = 0
		print('할인권을 사용하지 않았습니다')
		break
	else:
		usage = input('잘못된 입력입니다. 다시 입력해주세요: ')
		process = False

origin_price = people * 12000
sale_price = people * sale
total_price = origin_price - sale_price

print("")
print("<예매 상세 내역>")
print("==============================")
print("영화 제목: %s"%choice)
print("관람 인원: %d명"%people)
print("합산 금액: %d원"%origin_price)
print("할인 금액: %d원"%sale_price)
print("------------------------------")
print("실 결제액: %d원"%total_price)
print("==============================")
