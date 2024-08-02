# print('풍선')
# print("나비")
# print("ㅋ"*9)
# #불린은 참/거짓
# print(5>10)
# print(5<10)
# print(False)
# print(not True)
# print(not(5>10))
# #애완동물을 소개해 주세요~
# animal="강아지"
# name="연탄이"
# age=4
# hobby="산책"
# is_adult= age>=3
# print("우리집"+ animal+"의 이름은 "+name+"예요")
# print(name+"는" +str(age)+ "살이며," +hobby+ "을 아주 좋아해요.")
# print(name+ "는 어른일까요?" + str(is_adult))
# hobby= "공놀이"
# print("복습")
# print("우리집"+animal+"의 이름은 "+name+"이구요")
# print(name+"는" + str(age) +"살 이며," +hobby+ "를 아주 좋아해요")
# print(name+ "은 어른일까요?" +str(is_adult))
# # #'''이렇게하면 
# # 하단의 것이 모두 주석처리됨 '''
# station="사당"
# print(station+"행 열차가 들어오고 있습니다.")
# station="신도림"
# print(station+"행 열차가 들어오고 있습니다.")
# station="인천공항"
# print(station+"행 열차가 들어오고 있습니다.")
# print("연산")#연산
# print(2**3)#제곱 8
# print(5%3)#나머지 2
# print(5//3)#5의 몫 1
# print(10//3)#10의 몫 3
# print("비교 연산자")
# print(10>3)#T
# print(10<3)#F
# print(5<=5)#T
# print(3==3)#T
# print(3+4==7)#T
# print("조건자")#조건
# print(1!=3)#T
# print(not(1!=3))#F
# print((3>0)and(3<5))#t 둘다 만족해라
# print((3>0)&(3<5))#t 둘다 만족해라
# print((3>0) or (3>5))#t 둘중 하나만 만족해라
# print((3>0) | (3>5))#t 둘중 하나만 만족해라

# number=2+5
# print(number)
# number = number+3
# print(number)
# number += 3
# print(number)

# #숫자처리함수
# print("숫자처리함수")
# print(abs(-5))#절댓값
# print(pow(4,2))#a의b제곱으로 4^2 = 4*4=16
# print(max(1,2))#둘중의 최댓값
# print(min(1,2))#둘중의 최솟값
# print(round(4.7))#반올림
#from math import *
# print(floor(4.7))#내림
# print(ceil(4.7))#올림
# print(sqrt(16))#제곱근 
##------------------------------------------------------------------------------------
##랜덤함수
from random import *
# print("랜덤함수")
# print(random())
# print(random()*45)
# print(int(random()))#0~1
# print(int(random()*45))#0~44
# print(int(random()*45))#0~44
# print(int(random()*45)+1)#1~45
# print(randrange(1,45))#randrange 1~44. 정수이네?
# print(randint(1,45))#randint 1~45. 정수

# from random import *
# offline = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월"+ str(offline) +"일로 선정되었습니다.")

# a=4
# print(a)
# print(4*2)
# print(str(4*2))
# sentence='나는 소년입니다'
# print(sentence)
# sentence2="나는 소녀입니다"
# print(sentence2)
# sentence3="""나는 소녀이고 
# 파이썬은 쉬워요
# """
# print(sentence3)

# jumin="990210-1234567" #컴퓨터에선 0부터 센다.
# print("성"+jumin[7])#성별
# print("연"+jumin[0:2])#연_2글자 #[a:b] a부터 b직전까지
# print("월"+jumin[2:4])#월_2글자 
# print("일"+jumin[4:6])#일_2글자
# print("주민앞번호"+jumin[:6])#처음부터 6번째직전까지
# print("주민뒷번호"+jumin[7:])#7번째부터 끝까지
# print("주민뒷번호"+jumin[-7:])#맨뒤 7번째부터 끝까지 #뒤를 세는건 -1부터 센다

# python = 'Python is Amazing'
# print(python)
# print(python.lower())#변수선언 소문자로 바꿔라
# print(python.upper())#변수선언 대문자로 바꿔라
# print(python[1].isupper())#python의 하나문자 찝고, 대분자인지 확인하라.
# print(len(python))#python이 몇개의 문자인가.(공백포함)
# print(python.replace("Python","Java"))#python에서 a를 b로 바꿔라
# #---------------------------------------------------------------------------
# index=python.index("n") #n이란 글자가 index 즉 몇번째 있는지 인덱스하라.
# print(index)#그 번호를 출력하라.
# index=python.index("n",index+1)  #n다음에 있는 n의 순서로 index를 변경하여라
# print(index)#인덱스를 출력하여라.(답.15)
# print(python.find("java"))#java란 글씨가 있는지 찾아라(-1은 F란뜻)
# #print(python.index("java"))#java란 글씨가 있는지 인덱스로 찾아라(오류)
# print(python.count("n"))#n의 갯수를 구하라 

# #1. %를 이용하여 (d,s,c) print구문 만들기
# print ("나는 %d 살입니다." %10) 
# print("나는 %s색과 %s색을 좋아해요"%("빨간","파란"))
# print("나는 %c입니다."%"김")
# #2.2개의 구조 %문자열 만들기./
# #[]와 fomat으로 0과 1로 순서 정해보기/문장안에서 변수선언해보기/ 문장밖변수선언 불러오기
# print('나는 %s랑 %s 좋아해' %("떡볶이","칼국수"))
# print("나는 {}랑 {} 좋아해" .format("떡볶이","칼국수"))
# print("나는 {}를 좋아해".format('떡볶이'))
# print("나는 {1}와 {0}를 좋아해".format("떡볶이","칼국수"))
# print("나는 {a}와 {b}를 좋아해" .format(a="떡볶이",b="칼국수"))
# a="냉면"
# b="고기"
# print(f"나는 {a}과 {b}를 좋아해")

#\n:줄바꿈(키보드에서 \는 원화표시로 돼있음)
#-----------------------------------------------------------------------------------
#섹션5 제어문
# print("섹션5 제어문")
# w =input("오늘 날씨 어때요?")
# if w =="비" or w=="눈":
#     print("우산을 챙기세요")
# elif w=="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요없삼")
# temp=int(input("기온은 어때요?")) #int는 숫자답쓸수있는 지문
# if 30<=temp:
#     print("쩌죽을지도 나가지마세요")
# elif 10<=temp<30: #10<=temp and temp<30: 이렇게도 가능 
#     print("지금이야! 외출하자")
# elif 0<=temp<10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추우니 나가지 마세요")

#for_반복해서 사용할때
# for wating_no in [0,1,2,3,4,5,6]:
#     print("대기번호: {}".format(wating_no))
#randrange()
# for waiting_no in range(5): #1,2,3,4,5
#     print("대기번호:{}".format(waiting_no))
# for waiting_no in range(2,6): #대기순서를 2부터 6번째 이전까지 하고싶다
#     print("대기번호:{}".format(waiting_no))

# starbucks=["아이언맨","토르","그루트"] #스타벅스에 아이언맨,토르,그루트가 왔다.
# for customer in starbucks :   #for in으로 리스트를 불러오고 
#    print ("{},커피가 준비되었습니다.".format(customer)) #print로 출력해라(.format)

#while
# customer="토르"     #토르라는 손님 변수선언
# index=5             #인덱스의 번호를 5개
# while index>=1:     #와일은 조건을 만족할때까지 반복하란뜻 
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer,index))#프린트, {손님} 커피가 준비되었습니다. {몇}번남았어요.포멧(~,~)
#     index-=1 #인덱스를 한번씩 줄여나간다. 
#     if index==0 : #만약 인덱스가 0이되면
#         print("커피는 폐기처분되었습니다.")#프린트하라 커피는 폐기처분 되었습니다.

#while 어떤 카페는 손님이 올때까지 준비됬다고만말한다.
# customer="아이언맨" #아이언맨 변수선언
# index=1             #인덱스는 1
# while True:         #올때까지는 조건이 없으니 와일 트루
#     print("{0},커피가 준비되었습니다.{1}번째 호출".format(customer,index))#프린트, {}커피가 준비되었습니다.
#     index+=1        #인덱스번호는 확인차 1씩 더해지는것으로 ~~~무한루프 나옴 //키보드 ^+c누르면 강종됨

# #while 이름같지않으면 반복
# customer="장상준"#손님변수선언
# person="??" #펄슨은 언노운 변수선언
# while customer != person :                        #손님이름이 다르다면 계속 반복하여라
#     print ("{}님,커피가 준비되었습니다.".format(customer))#print 손님의 이름을 말하고
#     person= input("성함이..?")                  #이름이 어떻게 되는지 인풋값으로 질문하고 그 답값을 펄슨에 저장하여라
# #이름이 같다면 반복문에서 탈출

#continue와 break
# absent=[2,5]#두명 결석
# nobook=[7]#두명 책안가져옴
# for student in range(1,11): #포 스튜던스 변수선언해서 1~10렌지로 영역 설정
#     if student in absent:   #만약 지금 리스트안 학생이 결석했다면
#         continue            #컨티뉴 (스킵하고 진행하란뜻, 다음 반복으로 진행하라)
#     elif student in nobook: #_앞에사이에_ 만약 학생이 책안가져온 학생이라면
#         print("수업은 여기까지.{}은 교무실로".format(nobook))#프린트 오늘수업은 여기까지 0은 교무실로 팔로우
#         break                #브레이크(반복안하고 멈춤, 종료)
#     print("{},책을 읽어봐".format(student))#프린트 0, 책읽어봐

# #한줄for
# #출석번호가 1,2,3,4 앞에 100을 붙이시오 
# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student]
# print(student)
# #학생 이름을 길이로 변환해서 출력하시오
# student = ["Iron man","Thor","Groot"]
# student = [len(i) for i in student ]
# print(student)
# #학생 이름을 대문자로 변환하여 출력하시오
# student = ["Iron man","Thor","Groot"]
# student = [i.upper() for i in student ]
# print(student)

# #Quiz) 50명의 승객과 매칭기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시요
# #조건1: 승객별 운행소요기간 5~50분 사이의 난수
# #조건2: 당신은 소요시간 5분~15분 승객만 매칭해야 한다. 
# #[0] 20번째 손님 (소요시간 : 6)       
# #[] 21번째 손님 (소요시간 : 20)   
# from random import *
# cnt=0 #총 탑승 승객수
# for i in range(1,51): #1~50 승객수
#     time = randint(5,50) #5~50분 소요시간
#     if 5<=time<=15 :
#         print ("[0] {0}번째 손님 (소요시간 : {1})".format(i,time))
#         cnt += 1 
#     else :  #매칭 실패
#         print ("[] {0}번째 손님 (소요시간 : {1})".format(i,time))
# print("총 탑승 승객 {}명".format(cnt))

#----------------------------------------------------------------------------
# #numpy 독학
# import numpy as np
# # 1차원 배열 생성
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([6, 7, 8, 9, 10])
# # 배열 연산 수행
# arr_sum = arr1 + arr2
# arr_diff = arr1 - arr2
# arr_product = arr1 * arr2
# arr_division = arr1 / arr2
# # 결과 출력
# print("Sum:", arr_sum)
# print("Difference:", arr_diff)
# print("Product:", arr_product)
# print("Division:", arr_division)

# import numpy as np
# A=np.array([[1,2],[3,4]])
# B=np.array([0,1])
# C=A+B
# D=C*2
# final_result=D-1
# print(final_result)

# import numpy as np
# import pandas as pd

# data = np.array([[10,20,np.nan],[30,np.nan,60],[50,80,90]])
# df=pd.DataFrame(data,columns=['A','B','C'])

# df.fillna(df.mean(),inplace=True)
# df['B']=(2*df['B'].astype(int))
# max_values=df.max().values
# sorted_max_values=np.sort(max_values)
# median_of_max_values=np.median(sorted_max_values)

# final_result=median_of_max_values
# print(final_result)

 
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance,money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money 

balance=0
balance=deposit(balance,1000)
print(balance)