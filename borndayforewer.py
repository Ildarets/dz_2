win = 'wrong'
while True:
    inp_age = int(input("Какой год рождения А.С. Пушкина? "))
    if inp_age == 1799:
        while True:
            inp_day = str(input("Какой у А.С.Пушкина день рожденья? "))
            if inp_day == '26 мая':
                win = 'right'
                print('Верно')
                break
    break

