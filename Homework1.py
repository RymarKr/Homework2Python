# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# 1 - герб, 0 - решка
# Ввод:
# 4 - число монет
# 0
# 1
# 1
# 1
# Вывод:
# 1

n = int(input())
count_zero = 0
coat_of_arms = 0

for i in range(n):
    b = int(input())
    if b == 0:
        count_zero += 1
    else:
        coat_of_arms += 1
if coat_of_arms > count_zero:
    print(count_zero)
else:
    print(coat_of_arms)


