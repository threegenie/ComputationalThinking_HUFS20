#실습1 사전 자료형
phones = {"model":"iPhone11","manufacturer":"Apple","year":"2019"}
print(phones.get("year"))
phones.clear()
print(phones)

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

