print('Введите массив: значения через пробел')
l = input().split()
final_list = []
for el in l:
    if len(el) <= 3:
        final_list.append(el)


print(*final_list, sep=' ')
