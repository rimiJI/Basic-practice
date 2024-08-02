# def f(x):
#     return  2*x+7

# def g(x):
#     return x**2

# x=2 

# print(f(x)+g(x)+f(g(x))+g(f(x)))
    

def f(x):
    print(x+10)

def g(y):
    return y+10
y=0
c=0

print(y) #0으로 출력
c=g(2)   #c의 값이 12로 할당 *새로운 값을 할당시키려면, 새로운 변수를 선언
print(c) #12로 출력
print(g(4)) #4+10=14로 출력