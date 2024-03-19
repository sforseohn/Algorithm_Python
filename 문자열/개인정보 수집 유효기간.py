MONTH = 28

def cal_diff(today, day):
    day = list(map(int, day.split(".")))

    y = today[0] - day[0]
    m = today[1] - day[1]
    d = today[2] - day[2]
    
    diff = y * MONTH * 12 + m * MONTH + d
    return diff
    
    
def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split(".")))

    # 약관 딕셔너리 만들기
    term_dict = dict()
    for t in terms:
        term_type, term = t.split()
        term_dict[term_type] = int(term)
        
    # 개인정보마다 계산
    for i in range(len(privacies)):
        day, term_type = privacies[i].split()
        diff = cal_diff(today, day)
        
        if diff >= term_dict[term_type] * MONTH:
            answer.append(i + 1)
        
    return answer