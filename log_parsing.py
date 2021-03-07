"""
로그 예시
2016-09-15 hh:mm:ss.sss 처리시간 
2016-09-15 01:00:04.002 2.0s
처리시간은 시작시간과 끝시간을 포함한다!  
1. 파싱
2. 
3. 최댓값만 반환
"""
from datetime import datetime, timedelta   

def check(time, moment):
    start = time
    end = time + timedelta(milliseconds=999)
    # 구간 안의 로그 찾기 
    # 구간 시작 보다 늦게 시작하고, 구간 시작 보다 늦게 끝남 
    if start >= moment[0] and start <= moment[1]:
        return True 
    # 구간의 끝보다 로그가 늦게 시작하고, 구간의 끝보다 로그가 빨리 찍히는 경우 
    elif end >= moment[0] and end <= moment[1]:
        return True
    # 구간의 시작보다 로그의 시작이 느리고, 구간의 끝이 로그의 끝보다 긴 경우 
    elif start <= moment[0] and end >= moment[1]:
        return True

    return False


def solution(lines):
    result = []
    for line in lines:
        temp = line.split(' ')
        # 2016-09-15 hh:mm:ss.sss 처리시간 에서 
        # 시간만 간져오기 
        date = str(temp[0]) + " " + str(temp[1])

        # 예외처리 코드 추가... 
        # 2.0s 와 2s가 있음... 
        if '.' in temp[2]:
            delay = temp[2].split('.')
            delay[1] = delay[1][0:-1]
        else:
            delay = list(temp[2][0:-1])
            delay += ["0"]

        #yyyy-mm-dd 를 date 객체(yyyy,mm,d)로 변환
        #완료시간은 로그에 찍힌 대로 
        end = datetime.fromisoformat(date)

        # 시작시간은 완료시간에서 처리시간을 뺀 만큼  
        # 중요 ! 처리시간은 시작시간과 끝시간을 포함이므로 
        # 처리시간 T에서 밀리새컨드에 delay[1] - 1을 해주어야 함
        start = end - timedelta(seconds=int(delay[0]), milliseconds=int(delay[1]) - 1)

        result.append([start, end])
    #요청량     
    answers = []
    for timelist in result:
        for time in timelist:
            answer = 0
            #로그의 시작시간 끝시간으로부터 처리량 비교 
            for moment in result:
                if check(time, moment) == True:
                    answer += 1
            answers.append(answer)   

    # 최대 처리량만 반환 
    return max(answers)
