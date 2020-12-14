# 1. for 반복문을 while 반복문으로 변환
n = int(input("정수를 입력하시오: "))

fact = 1
i = 1
#for i in range(1, n+1):     # for 문 -> while 문으로 변환
while(i<=n):
	fact = fact * i      # for 문 -> while 문으로 변환
	i += 1
		
print(n, "!은", fact, '이다.')

#2. 달을 입력 받아서 계절명을 출력하기
month = int(input())

if(month==3 or month==4 or month==5):
	print("봄")
elif(month==6 or month==7 or month==8):
	print("여름")
elif(month==9 or month ==10):
	print("가을")
elif(month==11 or month==12 or month==1 or month==2):
	print("겨울")
else:
	print("계절을 출력할 수 없습니다.")

#3. 문자열 함수를 사용하여 문자열 찾기 및 계산
Edu_Ph = """
Inspired by the idea of free democracy, HUFS encourages the development of students’ 
individuality and builds their leadership character to make them highly capable 
people of the kind who can contribute to the development of Korea and the world. 
In the process, it never strays from its founding spirit of "truth, peace, and creation."
HUFS is also moving to establish its independence as a private school while never 
losing sight of its nature as a public educational institution. In addition, 
HUFS seeks to differentiate itself from other institutions of higher education and 
maintain its distinctiveness, as manifested in its school name."""

one = Edu_Ph.count("school")
two = Edu_Ph.find("HUFS")
three = Edu_Ph.rfind("its")

print(one, two, three, two+three, three//two, three%two)

#4. 중첩 반복문을 사용하여 다음과 같이 출력하는 코드를 작성
user_input = int(input("정수를 입력하시오: "))

list = ""

for i in range(1, user_input+1):	
	if i%2==1:
		list+=str(i)	
	elif i%2==0:
		list+=("*")
	i+=1
	print(list)
