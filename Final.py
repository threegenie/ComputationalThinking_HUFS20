#4번 문항은 일단 결과는 나왔지만 전역변수랑 지역변수 사용을 제대로 했는지가 의문..
#실제로 구름 채점상으로는 0점 나온 코드다ㅠㅠ 마음아파.. 아마 부분점수를 주실 것 같다!

#1 리스트의 처리 
lists = [105, 28, 54, 201, 15, 123, 87, 186, 247]
new_list = []

##  for 반복문과 조건문을 사용하여 아래에 프로그램을 작성하시오
for i in range(len(lists)):
	if lists[i]%3==0:
		new_list.append(lists[i])
		
print('결과 :', new_list)
print('합계 :', sum(new_list))


#2 딕셔너리를 활용하여 반복 횟수 계산 

lists = [4,3,6,9,5,8,1,8,9,9,5,7,5,5,9,5,2,7,8,4,9,2,9,7,9,4,6,8,2,7]
count = {}    ## 딕셔너리로 선언

## 아래에 프로그램을 작성하시오.

for n in lists:
	if n in count:
		count[n] += 1
	else:
		count[n] = 1

print(count)  ## 결과를 딕셔너리로 출력

#3 함수의 이해 매개변수와 반환값 
## 함수 1  (배점 2점)
## 코드 작성
def get_max(a,b):
	return max(a,b)

## 함수 2  (배점 2점)
## 코드 작성
def repeat(a,n):
	return a*n

## 함수 3 (배점 2점)
## 코드 작성
def get_min(a,b):
	return min(a,b)

## 함수 4 (배점 2점)
## 코드 작성
def get_plus(a,b):
	return a+b


print(get_max(13, 36))      ## 함수 1 : 두개의 값 중에서 최대값을 반환하여 출력

print(repeat('hufs', 5))    ## 함수 2 : 'hufs' 를 5번 반복하여 출력

print(get_min(6, 12))       ## 함수 3 : 두개의 값 중에서 최소값을 반환하여 출력

print(get_plus(23, 65))     ## 함수 4 : 두개의 값의 합계값을 반환하여 출력

#4 전역변수와 지역변수 
def calc_rect1(x, y):   ## 지역변수를 사용하여 직사각형의 넓이를 구하는 함수를 작성
## 코드 작성 (배점 1.5점)
	return x*y

def calc_rect2(x, y):   ## 전역변수를 사용하여 직사각형의 넓이를 구하는 함수를 작성
## 코드 작성 (배점 1.5점)
	global area
	area = x*y
	return area
	
x = int(input("가로의 길이: "))
y = int(input("세로의 길이: "))

## 지역변수로 작성한 calc_rect1() 함수를 사용하여 직사각형의 넓이를 실행화면과 같이 출력하는 프로그램을 작성
## 코드 작성 (배점 1.5점)
print(calc_rect1(x,y))

## 전역변수로 작성한 calc_rect2() 함수를 사용하는 직사각형의 넓이를 실행화면과 같이 출력하는 프로그램을 작성
## 코드 작성 (배점 1.5점)
print(calc_rect2(x,y))
