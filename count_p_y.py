def solution(s):
    answer = True
    s = s.lower()
    return s.count('p') == s.count('y')
