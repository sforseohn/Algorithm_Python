def get_shortened_length(s, unit_length):
    length = len(s)
    new_length = length
    prev = ""
    cnt = 1
    left = 0
    right = unit_length
    
    while right <= length:
        cur = s[left:right]
        
        if prev == cur:
            cnt += 1
        else:
            if cnt > 1: # 압축 가능
                new_length += len(str(cnt))
                new_length -= (cnt - 1) * unit_length # 반복 문자열 제외

            cnt = 1
            prev = cur
        
        left += unit_length
        right += unit_length
        
    if cnt > 1: # 남아있는 문자열 반영하기
        new_length += len(str(cnt))
        new_length -= (cnt - 1) * unit_length # 반복 문자열 제외
    
    return new_length


def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 1):
        answer = min(answer, get_shortened_length(s, i))
    
    return answer