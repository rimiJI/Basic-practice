#[PCCE 기출문제] 7번 / 가습기
def func1(humidity, val_set):
    if humidity < val_set:
        return 3
    return 1

def func2(humidity):
    if humidity >= 50:
        return 0
    elif humidity >= 40:
        return 1
    elif humidity >= 30:
        return 2
    elif humidity >= 20:
        return 3
    elif humidity >= 10:
        return 4
    else:
        return 5

def func3(humidity, val_set):
    if humidity < val_set:
        return 1
    return 0

def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func2(humidity)
    elif mode_type == "target":
        answer = func1(humidity, val_set)
    elif mode_type == "minimum":
        answer = func3(humidity, val_set)
    return answer



#[PCCE 기출문제] 5번 / 산책 /C++
'''이번은 C++로 풀었다.case에 관한 문제로 
single quots안에 표기함
#include <string>
#include <vector>

using namespace std;

vector<int> solution(string route) {
    int east = 0;
    int north = 0;
    vector<int> answer(2);
    for(int i=0; i<route.length(); i++){
        switch(route[i]){
            case 'N':
                north++;
                break;
            case 'S':
                north--;    <-이거빈칸문제였음
                break;
            case 'E':
                east++;    <-이거빈칸문제였음
                break;
            case 'W':
                east--;    <-이거빈칸문제였음
                break;    <-이거빈칸문제였음
        }
    }
    answer[0] = east;
    answer[1] = north;
    return answer;
}
'''


#[PCCE 기출문제] 3번 / 나이 계산
year = int(input())
age_type = input()

if age_type == "Korea":
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