import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Подбор 'загаданного' числа с помощью алгоритма бинарного поиска.
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток.
    """
    
    # Начальные условия
    count = 0                 # Количество попыток подбора  
    lower_search_limit = 1    # Нижняя граница диапазона поиска
    upper_search_limit = 101  # Верхняя граница диапазона поиска
    
    # Реализация алгоритма бинарного поиска в цикле while.
    while True:
        predict = int((lower_search_limit + upper_search_limit)/2)
        count += 1
        if predict > number:
            upper_search_limit = predict
        elif predict < number:
            lower_search_limit = predict
        else:                 # Условие выхода из цикла,
            break             # когда  predict == number
    
    return count


def score_game(test_funct_name) -> int:
    """Функция тестирования алгоритмов подбора 'загаданного' числа.
       Количество итераций, необходимое алгоритму для подбора числа. 
       Вычисляется среднее значение из 10000 ипытаний.

    Args:
        test_funct_name: Имя тестируемой функции для подбора числа

    Returns:
        int: среднее количество попыток
    """
    
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    # Формируем список 'случайных' чисел
    random_array = np.random.randint(1, 101, size=(10000))  
    
    # Формируем список количества попыток.
    count_ls = []
    
    for number in random_array:
        count_ls.append(test_funct_name(number))
    
    # Находим среднее значение количества попыток.
    score = int(np.mean(count_ls))
    attempt = len(count_ls)   # Количество испытаний
    
    print(f"При проведении {attempt} испытаний, этот алгоритм")
    print(f"угадывает число в среднем за {score} попыток.")

print('Run benchmarking for game_core_v3.')
score_game(game_core_v3)