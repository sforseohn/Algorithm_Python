def get_length(unit_length, s):
    length = len(s)
    new_length = length
    prev = ""
    cnt = 1
    left = 0
    right = unit_length
    
    while right <= length:
        cur = s[left:right]
        if cur == prev:
            cnt += 1
        else:
            if cnt > 1:
                new_length += len(str(cnt))
                new_length -= unit_length * (cnt - 1)
            prev = cur
            cnt = 1
            
        left += unit_length
        right += unit_length
        
    if cnt > 1:
        new_length += len(str(cnt))
        new_length -= unit_length * (cnt - 1)
    
    return new_length


def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 1): # i: 자를 단위
        ans = get_length(i, s)
        answer = min(ans, answer)
    
    return answer