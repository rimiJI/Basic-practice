






#[PCCE 기출문제] 3번 / 나이 계산
year = int(input())
age_type = input()

if age_type == "korea":
    answer = 2030-year+1

elif age_type == "Year":
    answer=2030-year

print(answer)


#[PCCE 기출문제] 4번 / 저축
start = int(input())
before = int(input())
after = int(input())

money = start
month = 1
while money < 70:
    money += before
    month += 1
while money < 100:
    money+=after
    month += 1

print(month)





# nums=list(map(int,input().split()))
# a=list(dict.fromkeys(nums))
# b=list(set(nums))
# print (a,'\n',b)









# import math
# print(math.comb(15,6))