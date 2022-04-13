from main import Start
from random import random

f = open('dataset.txt', 'w')

for _ in range(1000):
    Rand = random()
    for __ in range(1000):
        AI = random()
        f.write(str(AI) + ' ')
        f.write(str(Rand) + ' ')
        AIp, Randp = Start(AI, Rand)
        f.write(str(AIp) + ' ')
        f.write(str(Randp) + ' ')
        f.write('\n')

