#6주차 실습 1

i = 0
frog = int(input())

while(i<frog):
    print("개구리 %d마리" %(i+1))
    i+=1

#6주차 실습 2

num = int(input())
sum = 0

for i in range(1,num+1):
    if (i%2==0):
        sum+=i

print(sum)

#6주차 마무리 과제
start_day = 2  # Tuesday
last_day = 31

print('\tS\tM\tT\tW\tT\tF\tS')
for i in range(start_day) :
	print('\t', end='')
for i in range(1, last_day+1):
	if i%7 !=5 :
		print('\t%d' %i, end='')
	elif i%7 == :
		print('\t%d\n' %i)
	
