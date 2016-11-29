
import random

X = 'ACTG'

outfile = open('rand.txt', 'w')

for i in range(10000):
    seq = random.choice(X) +random.choice(X) +random.choice(X) +random.choice(X) +random.choice(X) +random.choice(X) +random.choice(X) +random.choice(X) +random.choice(X) +random.choice(X) +random.choice(X) +random.choice(X) + random.choice(X) + random.choice(X) + random.choice(X) + random.choice(X) + '\n'
    outfile.write(seq)