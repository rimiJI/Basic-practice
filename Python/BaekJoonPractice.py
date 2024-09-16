
# #괄호
# a=int(input())
# brackets=[]
# stack=[]

# for i in range(a):
#     brackets.append(input())

# def check(bracketElements):
#     for i in brackets:
#         for j in i:
#             if j=='(':
#                 stack.append(j)
#             elif j==')':
#                 stack.pop()
#     if len(stack)==0:
#         return print(True)
#     elif len(stack)!=0:
#         return print(False)
    
    
# print("----------Checking--------")
# print(check(brackets))

# 입력 받을 줄 수
a = int(input())

def check(bracket_elements):
    stack = []  # 각 괄호 문자열에 대해 스택을 초기화합니다.
    for char in bracket_elements:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

# 괄호 문자열을 입력받고 결과를 출력합니다.
for _ in range(a):
    brackets = input().strip()
    result = check(brackets)
    print(result)


