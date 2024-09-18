def solution(prices):
    answer=[]
    for i in range(1,len(prices)+1):
        if prices[i-1]>prices[i]:
            answer.append(len(prices)-i-(prices[i-1]-prices[i]))
        
        else:   
            answer.append(len(prices)-i)

    return answer