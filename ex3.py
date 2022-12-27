import time
from datetime import datetime

last_time = 0.0

def func_exec_time_frequency_log(func):
    def wrapper(*args):
        global last_time

        with open('func.log', 'a', encoding='utf-8') as log:
            if time.time() - last_time < 1.5:
                print('Слишком частый доступ к функции.')
                log.write(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}: {func.__name__}: Слишком частый доступ к функции.\n')
                return None

            start = time.time()
            value = func(*args)
            end = time.time()

            log.write(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}: {func.__name__} = {value} calculated in {start-end} s\n')

        last_time = time.time()
        return value
    return wrapper

@func_exec_time_frequency_log
def even_or_odd(number):
    '''Функция проверки целого числа на четность
    
    params: целое number
    returns: 
            True - число четное
            False - число нечетное
            None - ошибка
    '''
    try:
        number = int(number)
        if (number % 2 == 0):
            return True
        else:
            return False
    except (ValueError, TypeError):
        return None

# Не ругайтесь на бесконечный цикл, 
# это кусочек автоматизации проверки...

while (True):
    print(even_or_odd("4534"))
    time.sleep(2)
    print(even_or_odd(121))
    time.sleep(1)
    print(even_or_odd("sdfd"))
    time.sleep(2)
    print(even_or_odd(2344))
    time.sleep(1)
    print(even_or_odd("sdfddf"))
    time.sleep(1)
    print(even_or_odd(2341))
    time.sleep(2)

