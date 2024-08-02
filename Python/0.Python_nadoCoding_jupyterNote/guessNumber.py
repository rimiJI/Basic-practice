# 숫자를 맞춰보세요 (1 ~ 100)
# 50
# 숫자가 너무 큽니다
# 40
# 숫자가 너무 작습니다
# 30
# 숫자가 너무 작습니다
# 60
# 숫자가 너무 큽니다
# 50
# 숫자가 너무 큽니다
# 25
# 숫자가 너무 작습니다
# 40
# 숫자가 너무 작습니다
# 45
# 숫자가 너무 작습니다
# 48
# 정답입니다. 입력한 숫자는 48 입니다

print("숫자를 맞춰보세요 (1 ~ 100)")
num=int(input())
import random as rd
rdnum=rd.randint(1,100)

while num!=rdnum:
    if num>rdnum:
        print("숫자가 큽니다.")
        num=int(input())
    else:
        print("숫자가 작습니다.")
        num=int(input())
    # elif num<rdnum:
    #     print("숫자가 작습니다.\n")
    # else:
    #     print (f"정답입니다. 정답은 {rdnum} 입니다.")  #이렇게해도 나쁘지 않다.
print(f"맞췄습니다! 정답은 {rdnum} 입니다.")