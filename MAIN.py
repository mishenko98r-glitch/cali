def plus(a, d):
   return a + d
def misnys(a, d):
   return a - d
def delenie(a, d):
    return a / d
def df(a, d):
    return a * d

def pl(a, d):
   return a + d
def mi(a, d):
   return a - d
def de(a, d):
    return a / d
def dt(a, d):
    return a * d

def p(a, d):
   return a + d
def m(a, d):
   return a - d
def d(a, d):
    return a / d
def d(a, d):
    return a * d



def cfll():
    a = float(input("Введите 1 число: "))
    d = float(input("Введите2 число: "))
    f=float(input("Введите 3 число: "))
    g=float(input("Введите 4 число: "))
    h=float(input("Введите 5 число: "))
    j=float(input("Введите 6 число: "))

    print("\nВыберите операцию:")
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Деление")
    print("4 сложить и вычесть  3 числа ")
    print("5 сложить и сложить  4 числа")
    print("6 сложить и умножить  5 числа ")
    print("7 сложить и делить  6 числа ")
    print("8 Вычить и столожить  6 числа ")
    print("9 Вычить и умножить  6 числа ")
    print("10 умножить и вычесть  6 числа ")
    print("11 умножить и сложить  6 числа ")
    print("12 умножить и  делить  6 числа ")
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
        result = plus(a, d)

        print(f"\nРезультат деления: {a} + {d} = {result}")
    elif o == "5":
        result = plus(a, d)
        print(f"\nРезультат деления: {a} + {d} = {result}")
    elif o == "6":
        result = plus(a, d)
        print(f"\nРезультат деления: {a} + {d} = {result}")
    elif o == "7":
        result = plus(a, d)
        print(f"\nРезультат деления: {a} + {d} = {result}")
    elif o == "8":
        result = plus(a, d)
        print(f"\nРезультат деления: {a} + {d} = {result}")
    elif o == "9":
        result = plus(a, d)
        print(f"\nРезультат деления: {a} + {d} = {result}")
    elif o == "10":
        result = plus(a, d)
        print(f"\nРезультат деления: {a} + {d} = {result}")
    elif o == "11":
        result = plus(a, d)
        print(f"\nРезультат деления: {a} + {d} = {result}")

cfll()
