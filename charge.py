#다이나믹프로그래밍 문제
#tb[y][x] = money[0]~money[y]까지의 동전으로 x원을 만드는 방법의 갯수 
"""
우선 점화식 세우기 ! 
1,2원으로 5원을 만드는 방법을 알 때, 여기서 5원이 추가된 경우
[1,2,5]로 5원 만드는 방법
= [1,2]원으로 5원 만드는 방법
+ 전체금액에서 5원을 빼고, 남은 돈을 [1,2,5]원으로 방법
  (이 경우 0원이니 그냥 1개) 
즉, table[y][x] = table[y-1][x] + table[y][x-money[y]]
"""

def solution(n, money):
    tb = [[0 for _ in range(n+1)] for _ in range(len(money))]
    tb[0][0] = 1
    for i in range(money[0], n+1, money[0]):
        #초기화 
        tb[0][i] = 1
    for y in range(1, len(money)):
        for x in range(n+1):
            #점화식
            if x >= money[y]:
                tb[y][x] = (tb[y-1][x] + tb[y][x-money[y]]) %10000000007
            else:
                tb[y][x] = tb[y-1][x]
    return tb[-1][-1]
