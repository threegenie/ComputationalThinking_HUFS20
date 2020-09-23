#컴사고 4주차 실습1

print("\'비구름\'이 말했습니다.\n    \"비가 내리면 먼지가 사라질거야.\"")

#컴사고 4주차 실습2

year = int(input())
month = int(input())
date = int(input())
day = str(input())

print("오늘은 %d년 %d월 %d일 %s입니다." %(year,month,date,day))


#컴사고 4주차 실습2

sentence = "Contrary to popular belief, Lorem Ipsum is not simply random text."

num1 = sentence.count('t')
print(num1)

num2 = sentence.find('i')
print(num2)

print(sentence.upper())
print(sentence.lower())
print(sentence.replace('a','b'))


#컴사고 4주차 마무리 과제

num = 1 #포매팅에 사용할 유일한 변수
law = ("대한민국 헌법\n제1장 총강\n제1조\n	1. 대한민국은 민주공화국이다.\n	2. 대한민국의 주권은 \'국민\'에게 있고, 모든 권력은 \'국민\'으로부터 나온다.\n제2조\n	1. 대한민국의 \'국민\'이 되는 요건은 법률로 정한다.\n	2. 국가는 법률이 정하는 바에 의하여 재외\'국민\'을 보호할 의무를 진다.\n제3조\n	1. 대한민국의 영토는 한반도와 그 부속도서로 한다.")

print(law)
print(law.count('법률'))
print(law.index('주권'))
print(law.replace('대한민국','한국'))


#컴사고 계열별 예제 - 어문
foreign = '외래어'
print('%s 표기법' %foreign)

print('제1장 표기의 기본 원칙')

num = 1
print('제%d항 %s는 국어의 현용 %d 자모 만으로 적는다.' %(num, foreign, 24))

one = 1

print('제{0}항 {1}의 {2} 음운은 원칙적으로 {2} 기호로 적는다.'.format(num+1,foreign,one))

print(f'제{num+2}항 받침에는 \'ㄱ, ㄴ, ㄹ, ㅁ, ㅂ, ㅅ, ㅇ\'만을 쓴다.')

print(f'제{num+3}항 파열음 표기에는 된소리를 쓰지 않는 것을 원칙으로 한다.')

print('제{five}항 이미 굳어진 {0}는 관용을 존중하되, 그 범위와 용례는 따로 정한다.'.format(foreign, five=5))

rules = """외래어 표기법
제1장 표기의 기본 원칙
제1항 외래어는 국어의 현용 24 자모 만으로 적는다.
제2항 외래어의 1 음운은 원칙적으로 1 기호로 적는다.
제3항 받침에는 'ㄱ, ㄴ, ㄹ, ㅁ, ㅂ, ㅅ, ㅇ'만을 쓴다.
제4항 파열음 표기에는 된소리를 쓰지 않는 것을 원칙으로 한다.
제5항 이미 굳어진 외래어는 관용을 존중하되, 그 범위와 용례는 따로 정한다."""

print(rules.count('외래어'))
print(rules.find('외래어'))
print(rules.index('외래어'))
print(rules.find('한국어'))

print(rules.replace('외래어','한국어'))

#컴사고 계열별 예제 - 상경

print('A 기업의 달력 제품 광고비에 따른 판매액')

base = 2
print('%c = %d%c + %d' %('y', base, 'x', base * 2))

unit = '만원'
seed = 2
income = 2*seed+4

ad = '광고비'
sell = '판매액'
print(f'\t{ad}를 {seed}{unit} 사용하면 {sell}은 {income}{unit}이다.')

seed = 4
income = 2*seed+4
print(f"\t{ad}를 {seed}{unit} 사용하면 {sell}은 '{income}{unit} 이상'이라고 예측할 수 있다.")

print('\t{1}이 {income}{2}인 경우 {0}를 {seed}{2} 사용했다고 말할 수 있다.'.format(ad, sell, unit, seed = 8, income=20))


explain = """A 기업에서 판매하는 달력의 월 광고비와 판매액은 다음과 같은 관계를 갖습니다.
판매액(Y) = 2 * 광고비(X) + 4
예를 들어 광고비가 3만원이면 판매액은 10만원이 될 것이고,
반대로 판매액이 16만원이면 광고비는 6만원임을 유추할 수 있습니다."""

print(explain.count('광고비'))
print(explain.find('달력'))
print(explain.index('달력'))
print(explain.replace('판매금', '판매액'))

#컴사고 계열별 예제 - 자연
print('저항 R은 전압 V를 전류 I로 나눈 값이다.')
print('%c = %c / %c'%('R','V','I'))

RR = '저항'
VV = '전압'
II = '전류'
print('%s = %s / %s' %(RR,VV,II))

val_V = 1
print(f'\t{RR} R1은 {val_V}/0.4={val_V/0.4}, {RR} R2는 {val_V}/0.2={val_V/0.2}, {RR} R3는 {val_V}/0.1={val_V/0.1}이다.')

print(f'\t3개의 {RR} 중 가장 값이 큰 {RR}은 \'R3\'라고 할 수 있다.')

print('\t만약 {0} R4가 {3}V의 {1}을 받았을 때 {2}가 0.5A라면, 4V의 {1}을 받았을 때의 {2}는 {R4_A}A일 것이다.'.format(RR,VV,II,val_V,R4_A=4/2))

explain = """엄의 법칙은 전자기학의 가장 기본적인 법칙 중 하나로,
전자의 흐름인 전류는 저항값에 반비례하고 전압에 비례한다는 법칙이다.
독일의 물리학자 엄이 발견해 그의 이름을 따서 만들었다."""

print(explain.count('엄'))
print(explain.find('엄'))
print(explain.index('엄'))
print(explain.replace('엄','옴'))

