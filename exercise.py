print('Введите массив: значения через пробел')
l = [el for el in input().split()]
final_list = []
for el in l:
    if len(el) <= 2:
        final_list.append(el)


print(*final_list, sep=' ')
