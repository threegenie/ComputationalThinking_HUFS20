#실습 1 리스트 수정과 삭제

numbers = [10, 24, 52, 6, 30, 15, 2, 19, 27, 22]

numbers[0] = 40
print(numbers)

numbers[5] = 'hello'
print(numbers)

numbers[2:4] = ['b','i','g']
print(numbers)

numbers[2:7] = []
print(numbers)


#실습 2 리스트 함수

num_list = [1, 9, 2, 3, 4, 5, 7]

num_list.sort()
print(num_list)

num_list.remove(9)
print(num_list)

num_list.insert(5,6)
print(num_list)

num_list.append(8)
print(num_list)

num_list.sort(reverse=True)
print(num_list)

#실습 3 리스트 활용
mylist = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10], [11, 12]]

for i in range(len(mylist)):
    if len(mylist[i]) == 3:
        print(mylist[i])

#10주차 마무리 과제
answer = input()

total = 0
current = 0

for i in range(len(answer)) :
    if answer[i]=='O' :
        current +=1
	total += current

    elif answer[i]=='X' :
	current = 0
	total += current
	
print(total)
