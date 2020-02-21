# Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.

work_list = [2, 2, 5, 12, 8, 2, 12]
for number in work_list:
    if work_list.count(number) > 1:
        while work_list.count(number) > 0:
            work_list.remove(number)
print(work_list)
