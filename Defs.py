from Settings import *


class Player:
    def __init__(self, name):
        self.name = name
        self.past_capital = 0
        self.capital = 0
        self.current_price = 0
        self.produced_goods = 0
        self.sold_goods = 0
        self.clients = 0


def end_of_quarter(cp):
    cp.produced_goods = start_capital // cost_price
    clients_left = 0
    if cp.produced_goods >= cp.clients:
        cp.sold_goods = cp.clients
        cp.capital = cp.sold_goods * (cp.current_price - cost_price) - cost_price * (cp.produced_goods - cp.clients)
    else:
        cp.sold_goods = cp.produced_goods
        cp.capital = cp.sold_goods * (cp.current_price - cost_price)
        clients_left = cp.clients - cp.produced_goods

    return clients_left
