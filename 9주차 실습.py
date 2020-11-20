
#9주차 실습 - 인덱싱과 슬라이싱
my_list = ['a', 1, 2, 3, 'b', ['banana'], 4]

print(my_list[3])
print(my_list[0:6])
print(my_list[5])

#9주차 실습 - 리스트에 대하여
group = ['A', 'B', 'C', 'D', 'E', 'F']
name = ['가영', '나은', '다희', '라율']

all_list = [group[0], name[0:2], group[1:4], name[2], group[4:6], name[3]]
print(all_list)

#9주차 마무리 과제
num_list = []
sum=0

while True:
        num = int(input('몇 개를 입력하시겠습니까?'))
	
	if (num<0):
		print('다시 입력하세요')
	else:
		break

	
for i in range(num):
	data = int(input('넣을 숫자를 입력하세요:'))
		#num_list += data	
	num_list.append(data)
	sum += data
						 
print(num_list)
print('총합: %d' %sum)
