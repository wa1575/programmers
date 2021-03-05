from itertools import combinations

def solution(relation):
    answer = 0
    n_row = len(relation)
    n_col = len(relation[0])

    candidates = []
    for i in range(1, n_col+1):
        candidates.extend(combinations(range(n_col),i))

    #유일성만족하는 것 찾기, 튜플활용 
    uniq = []
    for candi in candidates:
        tmp = [tuple([item[i] for i in candi]) for item in relation]
        if len(set(tmp))==n_row:
            uniq.append(candi)

    #최소성 만족시키기 
    answer = set(uniq)
    for i in range(len(uniq)):
        for j in range(i+1,len(uniq)):
            if len(uniq[i]) == len(set(uniq[i]) & set(uniq[j])):
                answer.discard(uniq[j])


    return len(answer)
