s = input()
def balans(S):
    cnt_1 = cnt_2 = 0
    for i in range(len(S)):
        if s[i] == ')':
            cnt_1 += 1
        if s[i] == '(':
            cnt_2 += 1
    if cnt_1 == cnt_2:
        return 'Все хорошо'
    return 'Нет'
print(balans(s))
            
