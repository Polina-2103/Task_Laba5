from random import randint
while True:
    try:
        n = int(input('Введите число: '))
        break
    except ValueError:
        print('Введите целое число')

A = [randint(-100, 100) for i in range(n)]
print(A)
mx = A[0]
ind = cnt =  0
for i in A:
    print(i)
    if abs(i) > mx:
        mx = abs(i)
        ind = cnt
    cnt += 1

c = 0
s = 1
for i in A:
    if c == ind + 1:
        for i in A[c:]:
            s *= i
    c += 1
#1 Произведение чисел после max
print(s)

summ = c = 0
for i in A:
    if i < 0:
        for j in A[c+1:]:
            if j > 0:
                summ += j
            else:
                break
        break    
    c += 1
# Сумма расположенная между 1 и 2 отрицательными эл-ми
print(summ)

    

    
