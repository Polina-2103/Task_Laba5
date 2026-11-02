S = input().lower()
def spl(s):
    Words = []
    w = ''
    for i in s:
        if i == ' ':
            if w:
                Words.append(w)
                w = ''
        else:
            w += i
    if w:
        Words.append(w)
    return Words

W = spl(S)
cnt_g = 0
#print(W)
for i in W:
    if i[0] in 'еуёэоаыяиюeyuioa':
        cnt_g += 1
print(cnt_g)
    
