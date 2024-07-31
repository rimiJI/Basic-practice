#기초수학과 미적분
##1-1
my_value = 2*(3+2)**2/5-4
print(my_value)

##이것보다

##1-2
my_value2 = 2*((3+2)**2/5)-4
print(my_value2)

#세타=theta:각도를 의미
#베타=beta: 선형회귀의 매개변수로 사용
#1-4
theta = 1.75
beta=30.0

#변수에 첨자붙이면 인스턴스를 의미 x1,x2,x3 처럼
x1=3
x2=10
x3=44

#함수: 두개이상의 변수간의 관계
#입력변수input var= 도메인변수domain var=독립변수 independent var
#출력변수output var=종속변수dependent variable

#y=2x+1
#f(x)=2x+1

#1-6 파이썬에서 선형함수
def f(x):
    return 2*x+1

x_values=[0,1,2,3]

for i in x_values:
    y=f(i) # 1\n3\n5\n7
    print(y)

#y=2x+1은 연속함수=선형함수이다. 
#데카르트 좌표계cartesian coordinate system = xy평면 = 좌표평면coordinate plane

#1-7 심파이로 선형함수 그래프 그리기
from sympy import *
x=symbols('x')
f=2*x+1
plot(f)



