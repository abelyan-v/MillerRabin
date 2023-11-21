import random

#ввод чисел
n = 523 #число
k = 5000 #количество итераций

def table(n):
    PrimeNumbersFile = open('PrimeNumbers.txt', 'r')
    if (n < 10000):
        try:
            PrimeNumbers = PrimeNumbersFile.read()
        finally:
            PrimeNumbersFile.close()

        PrimeNumbersArrays = PrimeNumbers.split()
        if str(n) in PrimeNumbersArrays:
            print("Данное число является простым")
        else:
            print("Данное число является составным")
    else:
        print("Проверка данным методом недоступна, так как число больше 10000")

def get_s(n): #получение s
    s = 0
    n_for_while = n - 1
    while (n_for_while % 2 == 0):
        s = s + 1
        n_for_while = n_for_while / 2
    return s

def get_d(n, s): #получение d
    d = (n - 1) / pow(2, s)
    return d

def iteration(n, s, d, a): #итерация
    d = int(d)
    the_first_attempt = True
    print("a = " + str(a))
    for i in range(s):
        check = pow(2, i)
        check = check * d
        check = pow(a, check)
        check_with_mod = check % n
        print(" Проверка " + str(i) + ": a^2^s*d mod n = " + str(check_with_mod), end='')
        if (((check_with_mod == 1) & (the_first_attempt)) | (check_with_mod == n - 1)):
            print(", удовлетворяет условию")
            return True
        else:
            print(", не удовлетворяет условию")
            the_first_attempt = False
    return False

def ferm(n, k):
    coincidence = 0
    print("Проверка методом Ферма")
    for i in range(k):
        print("Итерация " + str(i + 1) + ":")
        a = random.randint(1, 100)
        print("a = " + str(a))
        check_with_mod = pow(a, n - 1) % n
        print("a^n-1 mod n = " + str(check_with_mod), end='')
        if (check_with_mod == 1):
            print(", удовлетворяет условию")
            coincidence = coincidence + 1
        else:
            print(", не удовлетворяет условию")
    print(str(coincidence) + " из " + str(k) + " итераций доказывает, что данное число является простым.")
    return coincidence

def nod(m, n):
    for x in range(m, 0, -1):
        if ((n % x == 0) & (m % x == 0)):
            return x

def calculateJacobian(a, n):
    if (a == 0):
        return 0
    ans = 1
    if (a < 0):
        a = -a
        if (n % 4 == 3):
            ans = -ans
    if (a == 1):
        return ans
    while (a):
        if (a < 0):
            a = -a
            if (n % 4 == 3):
                ans = -ans
        while (a % 2 == 0):
            a = a // 2
            if (n % 8 == 3 or n % 8 == 5):
                ans = -ans
        a, n = n, a
        if (a % 4 == 3 and n % 4 == 3):
            ans = -ans
        a = a % n
        if (a > n // 2):
            a = a - n
    if (n == 1):
        return ans
    return 0

def SoloveyShtrassen(n, k):
    coincidence = 0
    prime = True
    print("Проверка методом Соловея-Штрассена")
    for i in range(k):
        a = random.randint(3, n - 2)
        print("Итерация " + str(i + 1) + ":")
        print("a = " + str(a))
        nod_array = nod(a, n)
        print("Наибольший общий делитель (" + str(a) + ", " + str(n) + ") = " + str(nod_array), end="")
        if (nod_array == 1):
            print(", удовлетворяет условию")
        else:
            print(", не удовлетворяет условию")
            print("Значит, число " + str(n) + " является составным")
            prime = False
            break
        r = (n + calculateJacobian(a, n)) % n
        s_initial = (n-1) / 2
        s_initial = int(s_initial)
        s = pow(a, s_initial) % n
        print("r = " + str(r), end="")
        print(" s = " + str(s), end="")
        if (r == s):
            print(", удовлетворяет условию")
            coincidence = coincidence + 1
        else:
            print(", не удовлетворяет условию")
            print("Значит, число " + str(n) + " является составным.")
            prime = False
            break
    if (prime):
        posibility = 1 - pow(2, -k)
        print("Число " + str(n) + " является простым с вероятностью " + str(posibility) + ".")
    return coincidence

#начало программы
CoincidenceArray = []
coincidence = 0
if (n == 1):
    print("Это число на 100% не является простым, так как данное число является равное 1. Метод теста Миллера-Рабина не потребуется.")
else:
    if (n == 2):
        print("Это число на 100% является простым, так как исходное число равное 2. Метод теста Миллера-Рабина не потребуется.")
    else:
        print("Проверяется данное число из таблицы простых чисел")
        table(n)
        s = get_s(n)
        print("s = " + str(s))
        if (s == 0):
            print("Это число на 100% является составным, так как данное число является четным. Метод теста Миллера-Рабина не потребуется.")
        else:
            d = get_d(n, s)
            print("d = " + str(d))
            history = []
            for i in range(k):
                print("Итерация " + str(i + 1) + ":")
                a = random.randint(1, n - 1)
                coincidence_boolean = iteration(n, s, d, a)
                if (coincidence_boolean):
                    coincidence = coincidence + 1
                if (coincidence / k > 0.5):
                    IsPrimeString = "простым"
                else:
                    IsPrimeString = "составным"
            CoincidenceArray.append(coincidence)
            print(str(coincidence) + " из " + str(k) + " итераций доказывает, что данное число является простым.")
            print()
            coincidence = ferm(n, k)
            CoincidenceArray.append(coincidence)
            print()
            if (n != 3):
                coincidence = SoloveyShtrassen(n, k)
                CoincidenceArray.append(coincidence)
            print("---------------------------------------------------------------------------------------------")
            print()
            print("Общий результат проверки")
            print("Исходное число n = " + str(n))
            print("Количество итераций k = " + str(k))
            print("Количество итераций, которые доказали простоту чисел:")
            print(" Метод Миллера-Рабина: " + str(CoincidenceArray[0]))
            print(" Метод Ферма: " + str(CoincidenceArray[1]))
            if (n != 3):
                print(" Метод Соловея-Штрасена: " + str(CoincidenceArray[2]))
            print("Итог: в результате 3 методов обнаружено, что с большей вероятностью число " + str(n) + " является " + IsPrimeString)