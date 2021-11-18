def decator (func):
    def inner(n):
        print('Привет')
        func(n)
        print('Конец функций')

    return inner

def say(n):
    print('3',)


say = decator(say)
say('')
