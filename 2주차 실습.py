# 컴퓨팅사고 2주차 실습 1

a = input('')
print(a)

b = input('숫자를 1개 입력해주세요: ')
print(b)

c = 2.5

d = 100

e = 'c'

f = 'Hello hufs'

print(c, d, e, f)


# 컴퓨팅사고 2주차 실습 2

a = 10

b = 3.5

c = '안녕하세요.'

print(a, type(a))

print(b, type(b))

print(c, type(c))


# 컴퓨팅사고 2주차 마무리 과제 1

print('간단한 설문조사를 진행하겠습니다.')

name = input('1. 당신의 이름은 무엇인가요?')

number = input('2. 당신의 학번은 무엇인가요?')

major = input('3. 당신의 전공은 무엇인가요?')

place = input('4. 입학 후 학교에서 가장 먼저 방문한 곳은 어디인가요?')

event = input('5. 학교생활 중 가장 기대하는 것은 무엇인가요?')

print()
print('=====')

print(name, '님 안녕하세요.')
print(name, '님의 전공은', major, '이며, 학번은', number, '입니다.')
print(name, '님은 한국외국어대학교에서', place, '에 가장 먼저 방문하셨습니다.')
print(event, '을(를) 가장 기대하는', name, '님의 학교 생활을 응원합니다.')

print('=====')

# 컴퓨팅사고 2주차 실습 3

import turtle

turtle.shape('turtle')
## turtle.shape('classic')

turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)

turtle.done()

# 컴퓨팅사고 2주차 실습 4

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


