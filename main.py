from Defs import Player, cls, Players_move, end_of_quarter
from Version import __version__, Developers

players = []
number_of_players = 2  # int(input('Введите количество игроков: '))
# for i in range(number_of_players):
#     print('Введите ник игрока: ', end='')
#     players.append(Player(input()))
players = [Player('Nikita'), Player('Pavel')]

# print('Введите начальные условия:')
# start_capital = int(input('  Начальный капитал игроков: '))
# cost_price = int(input('  Себестоимость единицы товара: '))
# total_number_of_clients = int(input('  Количество жителей в городе: '))
# number_of_quarters = int(input('  Сколько кварталов будет длиться игра: '))
start_capital = 1000
cost_price = 1
total_number_of_clients = 30
number_of_quarters = 10
for player in players:
    player.capital = start_capital
    player.clients = total_number_of_clients // 2
left_clients = total_number_of_clients - (players[0].clients + players[1].clients)


end_of_game = False
for _ in range(number_of_quarters):
    if (players[0].capital < 0) or (players[1].capital < 0):
        end_of_game = True
        break
    Players_move(players[0])
    Players_move(players[1])
    if players[0].current_price > players[1].current_price:
        players[1].clients += round(players[0].clients * ((players[1].current_price / players[0].current_price) / 2))
        players[1].clients += left_clients
        players[0].clients -= round(players[0].clients * ((players[1].current_price / players[0].current_price) / 2))
    elif players[1].current_price > players[0].current_price:
        players[1].clients -= round(players[1].clients * ((players[0].current_price / players[1].current_price) / 2))
        players[0].clients += round(players[1].clients * ((players[0].current_price / players[1].current_price) / 2))
        players[0].clients += left_clients
    t = end_of_quarter(players[0])
    if t != 0:
        players[1].clients += t
    t = end_of_quarter(players[1])
    if t != 0:
        players[0].clients += t
        t = end_of_quarter(players[0])
        if t != 0:
            left_clients = t
    cls()

if end_of_game:
    if (players[0].capital < 0) and (players[1].capital < 0):
        print('Оба участника ужасные капиталисты. Это совместное поражение.')
    elif players[0].capital < 0:
        print('{0} обанкротился.\nПоздравляем с победой {1}!'.format(players[0].name, players[1].name))
    elif players[1].capital < 0:
        print('{0} обанкротился.\nПоздравляем с победой {1}!'.format(players[1].name, players[0].name))
else:
    if players[0].profit > players[1].profit:
        print('{0} смог заработать больше чем {1} и победил!'.format(players[0].name, players[1].name))
    elif players[0].profit < players[1].profit:
        print('{0} смог заработать больше чем {1} и победил!'.format(players[1].name, players[0].name))
    elif players[0].profit == players[1].profit:
        print('Оба участника прекрасные бизнесмены. Это победная ничья!'.format(players[0].name, players[1].name))
