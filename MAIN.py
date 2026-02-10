a = float(input("Введите первое число: "))
d = float(input("Введите второе число: "))
def plus(*args):
    print(args)
    result = 0
    for numder in args:
        result += numder
    return result

def delenie(*args):
    print(args)
    result = 0
    for numder in args:
        result += numder
    return result

def misnys(*args):
    print(args)
    result = 0
    for numder in args:
        result += numder
    return result

def fgfh(*args):
    print(args)
    result = 0
    for numder in args:
        result += numder
    return result



def cfll():


    print("\nВыберите операцию:")
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Деление")
    print("4 - умножение ")
    o = input("Введите номер операции 1-3: ")

    if o == "1":
        result = plus(a, d)
        print(f"\nРезультат сложения: {a} + {d} = {result}")
    elif o == "2":
        result = misnys(a, d)
        print(f"\nРезультат вычитания: {a} - {d} = {result}")
    elif o == "3":
        result = delenie(a, d)
        print(f"\nРезультат деления: {a} / {d} = {result}")
    elif o == "4":
        result = fgfh(a, d)
        print(f"\nРезультат деления: {a} * {d} = {result}")

cfll()