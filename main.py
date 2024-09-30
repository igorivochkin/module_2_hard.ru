# module_2_hard.ru

n = int(input('Число из первой вставки? '))
result = ""
for i in range(1, 20):
    for j in range(2, n):
        m = n%(i+j)
        if m == 0 and i != j and j > i:
            result=result+str(i)+str(j)
        continue
print(f'Для {n} искомый пароль, {result}')