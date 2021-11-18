def decorator(func):
    def inner(*args):
        print('Привет')
        func(*args)
        print('Конец функций')

    return inner

@decorator

def sum(n):
    n = n + 2
    print(n)

sum(1)