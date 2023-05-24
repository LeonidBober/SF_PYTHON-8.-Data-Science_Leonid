import numpy as np
def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    print(f'Первое число комп предположил - {predict}')
    
    #создадим 2 списка, в них будем хранить результаты подстановок
    #и сделаем их границами нашего поиска
    min_lst=[]#левая граница
    max_lst=[]#правая граница
    
    for i in range(0,15):# уменьшим зону поиска
        if predict < number:
            min_lst.append(predict)
            a = max(min_lst)
            predict = np.random.randint(a, 101)
            count +=1
        else:
            max_lst.append(predict)
            a = min(max_lst)+1
            predict = np.random.randint(1, a)
            count +=1
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    print (f"Комп угадал число {predict} за - {count} попыток")

    return count
game_core_v2(number = 80)
