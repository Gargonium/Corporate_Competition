class Player:
    def __init__(self, name):
        self.name = name
        self.past_capital = 0
        self.capital = 0
        self.current_price = 0
        self.profit = 0
        self.produced_goods = 0
        self.sold_goods = 0
        self.clients = 0
        print('(Добавлен игрок {0})'.format(self.name))


def cls():
    print('\n' * 100)


def Players_move(cp):
    print('Ход игрока {0}'.format(players[current_player].name))
    print('Текущая цена: ')
    print('Капитал: ')
    print('Прибыль за прошлый квартал: ')
    print('Количество клиентов: ')
    print('Доступные действия:\n 1. Изменить цену\n 2. Узнать прибыль соперника\n 3. Закончить')
    while True:
        action = input()
        if action == '1':
            cp.current_price += int(input('Увеличить на: '))
            if cp.current_price < 0:
                print('Цена не может быть отрицательной!!')
                cp.current_price = 0
                print('Текущая цена: 0')
        elif action == '2':
            for player in players:
                if player != cp:
                    print('{0}: {1}'.format(player.name, player.profit))
        elif action == '3':
            cls()
            break
        else:
            print('Пожалуйста, напишите номер действия из списка')


def end_of_quarter(cp):
    cp.produced_goods = cp.capital // cost_price
    clients_left = 0
    cp.past_capital = cp.capital
    if cp.produced_goods >= cp.clients:
        cp.sold_goods = cp.clients
        cp.capital = cp.sold_goods * (cp.current_price - cost_price) - cost_price * (cp.produced_goods - cp.clients)
    else:
        cp.sold_goods = cp.produced_goods
        cp.capital = cp.sold_goods * (cp.current_price - cost_price)
        clients_left = cp.clients - cp.produced_goods
    cp.profit = cp.capital - cp.past_capital
    return clients_left
