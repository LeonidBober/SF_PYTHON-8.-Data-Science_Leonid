#ГЕНЕРАЦИЯ FLOAT
import numpy as np
print(np.random.rand(3,5))
dd_=(2,3)

#в качестве аргумента именно кортеж без распаковки
print(np.random.sample(dd_))

#uniform(low=0.0, high=1.0, size=None)
print(np.random.uniform(5,10,size=(dd_)))

print(np.random.randint(6, 12, size=(3,3)))

arr = np.arange(6)
print(arr)
# [0 1 2 3 4 5]

#Просто перемешать все числа в массиве позволяет функция random.shuffle.
print(np.random.shuffle(arr))
# None
print(arr)
# array([0, 5, 1, 3, 2, 4])

#Чтобы получить новый перемешанный массив, 
# а исходный оставить без изменений, можно использовать функцию random.permutation. 
playlist = ["The Beatles", "Pink Floyd", "ACDC", "Deep Purple"]
shuffled = np.random.permutation(playlist)
print(shuffled)
# ['The Beatles' 'Pink Floyd' 'Deep Purple' 'ACDC']
print(playlist)
# ['The Beatles', 'Pink Floyd', 'ACDC', 'Deep Purple']

print(np.random.permutation(10))
# array([7, 8, 2, 9, 4, 3, 1, 0, 5, 6]) - (n-1)

#Чтобы получить случайный набор объектов из массива, используется функция random.choice:
#choice(a, size=None, replace=True)
workers = ['Ivan', 'Nikita', 'Maria', 'John', 'Kate']
 
choice = np.random.choice(workers, size=5, replace=False)
print(choice)

#SEED ГЕНЕРАТОРА ПСЕВДОСЛУЧАЙНЫХ ЧИСЕЛ (можно получать одинаковую случ последов)
np.random.seed(23)
print(np.random.randint(10, size=(3,4)))
# array([[3, 6, 8, 9],
#        [6, 8, 7, 9],
#        [3, 6, 1, 2]])

even = np.array(range (2,17,2))
mix = even.copy()


