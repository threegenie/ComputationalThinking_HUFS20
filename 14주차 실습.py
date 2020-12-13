#14주차 실습 파일 생성과 작성
#실습 특성상 테스트케이스가 없기 때문에 정답인지 아닌지 나오지 않는다ㅠㅠ
#그래서 내가 만든 코드가 정답인지는 모르겠지만ㅠ 일단 제출후 완료는 되는 코드..!!

A = [1,2,3,4,5,6,7,8,9,10]
A = sorted(A)
F = open('data/out.txt','w')
for i in A:
    data = F.write('%d'%i)
    F.write(data)
	
F.close()

#14주차 실습 파일 읽기와 내용 추가

f = open('data/meerkat.txt','r')

while True:
	data = f.readline()
	if not data:
		break
	elif '서식지' in data:
		print(data)
	
f.close()

#14주차 마무리 과제
f = open('data/about_python.txt','r')
sentences = []
i=0

while True:
	data = f.readline()
	if not data:
		break
	else:
		numbering = ('%d번 문장 '%(i+1))
		data = numbering + data
		sentences.append(data)
		i+=1
f.close()

f = open('data/about_python.txt','r')
for data in sentences:
	print(data, end='')
f.close()

