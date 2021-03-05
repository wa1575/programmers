def solution(clothes):
    answer = 1
    #dict 형태의 옷장
    closet = {}

    #종류별로 정리하기 
    #[의상의 이름, 의상의 종류] 형태로 받음 
    for ele in clothes:
        key = ele[1]
        value = ele[0]

        if key in closet:
            closet[key].append(value)
        else :
            closet[key] = [value]

    #조합 맞추기 -> 경우의 수  
    for key in closet.keys():
        answer = answer * (len(closet[key])+1) #+1은 벗는 경우 포함 

    # 모두 벗는 경우는 제외     
    answer -= 1  

    return answer
