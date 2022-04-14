from main import Start
from random import random

f = open('dataset.txt', 'w')

for _ in range(300):
    Rand = random()
    for __ in range(1000):
        AI = random()
        AIp, Randp = Start(AI, Rand)
        AI = int(AI * 1000)
        Rand = int(Rand*1000)
        Randp = int(Randp * 1000)
        AIp = int(AIp * 1000)
        f.write(str(AI) + ' ')
        f.write(str(Rand) + ' ')
        f.write(str(AIp) + ' ')
        f.write(str(Randp) + ' ')
        f.write('\n')
        Rand = Rand/1000

