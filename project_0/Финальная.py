""" Игра угадай число. 
Компьютер загадывает и угадывает число меньше чем за 20 попыток
"""

import numpy as np
def random_predict(number:int=1) -> int:
    """ Угадываем число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0
    lower_border = 0 #нижняя граница предпологаемого числа
    upper_border = 100 #верхняя граница предпологаемого числа
    predict_number = np.random.randint(1,101) #предпологаемое число
    while True:
        count +=1
        if number > predict_number:
            lower_border = predict_number
            predict_number = round((lower_border + upper_border)/2)
        elif number < predict_number:
            upper_border = predict_number
            predict_number = round((lower_border + upper_border)/2)
        else:
            break #выход из цикла
    return (count)
    
def score_game(random_predict) -> int:
    """За какое количество попыток  
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score
if __name__ == "__main__":
    # RUN
    score_game(random_predict)
 