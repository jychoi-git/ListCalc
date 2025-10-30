import math

def op(i, list):
    if i == 0: # 차원(길이)
        return len(list)
    if i == 1: # 합
        return sum(list)
    if i == 2: # 교대합
        return sum(list[j] if j % 2 == 0 else -list[j] for j in range(len(list)))
    if i == 3: # 제곱합
        return sum(x**2 for x in list)
    if i == 4: # 벡터길이
        return math.sqrt(sum(x**2 for x in list))
    if i == 5: # 최솟값 
        return min(list)
    if i == 6: # 평균 
        return sum(list) / len(list)
    if i == 7: # 최댓값 
        return max(list)
    if i == 8: # 중복 제거 후 개수 
        return len(set(list))
    if i == 9: # 표준편차 
        m = sum(list) / len(list)
        return math.sqrt(sum((x - m)**2 for x in list) / (len(list)-1))
    if i == 10: # 짝수합
        return  sum(x for x in list if x % 2 == 0)
    if i == 11: # 홀수합
        return  sum(x for x in list if x % 2 == 1)
        
