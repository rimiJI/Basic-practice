
# dan=int(input("구구단 몇단을 계산할까요?\n"))

# for i in range(0,10):
#     if dan==i:
#         for j in range(0,10):
#             # print("{0} X {1} = {2}".format(dan,j,dan*j))
#             print(f"{dan} X {j} = {dan*j}")
# else:
#     ("1~9 사이값을 입력하세요.")


# 구구단 몇 단을 계산할까요(1~9)?
# 5
# 구구단 5단을 계산합니다.
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# …..
# 5 X 8 = 40
# 5 X 9 = 45
# 구구단 몇 단을 계산할까요(1~9)?
# 10
# 0
# 구구단 게임을 종료합니다


dan = 5 #임의값

while dan!=0:
    print("구구단 몇 단을 계산할까요(1~9)?")
    dan = int(input())
    if 1 <= dan <= 9:      
        for i in range(1,10):
            print(f"{dan} X {i} = {dan*i}")
    
    elif dan > 9 :
        print("아잇 숫자가 너무 커요!!\n")

print("구구단 게임을 종료합니다........")


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n + factorial(n-1)
# print (factorial(int(input("Input Number for Factorial Calculation: "))))




