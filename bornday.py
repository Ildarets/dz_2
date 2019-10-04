while True:
    inp_age = int(input("Какой год рождения А.С. Пушкина? "))
    if inp_age == 1799:
        inp_day = str(input("Какой у А.С.Пушкина день рожденья? "))
        if inp_day == '26 мая':
            print('Верно')
            break
        print('Неверный день рождения')
        break
    print('Неверный год рождения')