def Start(AI, Rand):
    from Defs import Player, end_of_quarter
    from Version import __version__, Developers
    from random import random
    from Settings import start_capital, cost_price, total_number_of_clients, number_of_quarters

    players = []
    players = [Player('AI'), Player('Rand')]
    for player in players:
        player.capital = start_capital
        player.clients = total_number_of_clients // 2
    left_clients = total_number_of_clients - (players[0].clients + players[1].clients)

    players[1].current_price = (Rand+1)*cost_price
    players[0].current_price = (AI+1)*cost_price

    end_of_game = False
    for _ in range(number_of_quarters):
        if players[0].current_price > players[1].current_price:
            players[1].clients += round(players[0].clients * (players[1].current_price / players[0].current_price))
            players[1].clients += left_clients
            players[0].clients -= round(players[0].clients * (players[1].current_price / players[0].current_price))
        elif players[1].current_price > players[0].current_price:
            players[1].clients -= round(players[1].clients * (players[0].current_price / players[1].current_price))
            players[0].clients += round(players[1].clients * (players[0].current_price / players[1].current_price))
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

    return players[0].capital + random()*players[1].capital, players[1].capital+ random()*players[0].capital
