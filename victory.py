while True:
    right = 0
    person_1 = int(input('В каком году родилась Меган Фокс? ')) #1986
    person_2 = int(input('В каком году родилась Екатерина Новикова? ')) #1982
    person_3 = int(input('В каком году родился Cавелий Крамаров? ')) #1934
    person_4 = int(input('В каком году родилась Александра Трусова? ')) #2004
    person_5 = int(input('В каком году родилась Екатерина Вилкова? ')) #1984
    if person_1 == 1986:
        right+=1
    if person_2 == 1982:
        right += 1
    if person_3 == 1934:
        right += 1
    if person_4 == 2004:
        right += 1
    if person_5 == 1984:
        right += 1
    print('Количество правильных ответов {}'.format(right))
    print('Количество ошибок {}'.format(5-right))
    print('Процент правильных ответов {}'.format(right*100/5))
    print('Процент неправильных ответов {}'.format(((5-right)*100)/5))
    print("Хотите ли Вы начать игру сначала?")
    answer = input('Да/Нет ')
    if answer == 'Нет':
        exit()



