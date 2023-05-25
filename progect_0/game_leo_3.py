import numpy as np
def game_core_v2(number: int = 1) -> int:
    """_summary_

    Args:
        number (int, optional): случайно выбранное число компом. Defaults to 1.

    Returns:
        int: ЧИСЛО ПОПЫТОК
    """
    
    l_gr = 1 # левая граница
    r_gr = 100 # правая граница
        
    predict = np.random.randint(1, 101)# первое число, которое комп случайно выберет в наших границах
    count = 1 # счетчик попыток
    
    while number != predict: # бесконечный цикл
        if number > predict:
            l_gr = predict
            predict = np.random.randint(l_gr, (r_gr + 1))
            count +=1
        elif number < predict:
            r_gr = predict
            predict = np.random.randint(l_gr, (r_gr + 1))
            count +=1
            
    print(f'Комп угадал число - {number} за - {count} попыток')
            
    return count       
game_core_v2(100)      

    