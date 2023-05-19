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
    #a = 3
    for i in range(0,5):# располовиним несколько раз интервал и уменьшим зону поиска
        if predict < number:
            a = (100-predict) // 2
            predict += a
            count +=1
        else:
            a = (predict) // 2
            predict = a
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
