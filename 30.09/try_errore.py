
try:
    n = int(input('> '))
    if n == 100:
        raise TypeError('Число 100 запрещено к использованию')
    print(n)

except (ValueError, ZeroDivisionError):
    print('please enter a number')
except NameError:
    print('please enter a name')
except Exception as err: # неуказанная ошибка
    print(err)
else:
    print('когда нет ошибки')
finally:
    print('выполняется всегда')