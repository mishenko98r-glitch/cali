def plus(a, d):
    return a + d
def plus(a, d):
   return a + d
def misnys(a, d):
   return a - d

def cfll():
    a = float(input("Введите первое число: "))
    d = float(input("Введите второе число: "))

    print("\nВыберите операцию:")
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Деление")
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

cfll()