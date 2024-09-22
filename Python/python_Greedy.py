n=int(input())
def coin(c):
    count = 0  # 동전의 개수를 세는 변수

    while c > 0:
        if c >= 500:
            c -= 500
            count += 1  # 500원 동전을 사용했으므로 count를 1 증가시킴

        elif c >= 100:
            c -= 100
            count += 1  # 100원 동전을 사용했으므로 count를 1 증가시킴

        elif c >= 50:
            c -= 50
            count += 1  # 50원 동전을 사용했으므로 count를 1 증가시킴

        elif c >= 10:
            c -= 10
            count += 1  # 10원 동전을 사용했으므로 count를 1 증가시킴

    return count  

print(coin(n))