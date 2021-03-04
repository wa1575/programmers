def solution(s):
    answer = ''
    index = 0 
    for i in range(len(s)):
        if s[i] == ' ': #빈공간이면 
            index = 0
            answer += ' '
            continue
        elif index %2 == 0: #인덱스가 홀수이면(0포함) 
            answer += s[i].upper()
        else:  #그외, 인덱스가 짝수이면 
            answer += s[i].lower()

        index += 1 

    return answer
