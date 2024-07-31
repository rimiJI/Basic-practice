#선그리기
import matplotlib.pyplot as plt

#데이터 셋팅
x=[1,2,3,4,5]
y=[1,4,9,16,25]

#그래프 생성
plt.plot(x,y)

#그래프 제목과 축 레이블 추가
plt.title('Simple Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

#그래프 출력
plt.show()


#----------------------------

#막대 그래프 예제
import matplotlib.pyplot as plt

# 막대 그래프 예제
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.bar(categories, values)
plt.title('Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# 히스토그램 예제
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

plt.hist(data, bins=5)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

#-------------------------

#서브플롯 사용
x=[1,2,3,4,5]
y1=[1,4,9,16,25]
y2=[25,16,9,4,1]

plt.figure(figsize=(10,5))

#1번째 서브플롯
plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title('First Subplot')
# 두 번째 서브플롯
plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('Second Subplot')

plt.show()