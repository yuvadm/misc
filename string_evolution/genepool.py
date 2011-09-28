### http://www.electricmonk.nl/log/2011/09/28/evolutionary-algorithm-evolving-hello-world/

import random
import string
from time import sleep

source = "jiKnp4bqpmAbp"
target = "Hello, World!"

def fitness(source, target):
    fitval = 0
    for i in range(0, len(source)):
        fitval += (ord(target[i]) - ord(source[i])) ** 2
    return(fitval)

GENSIZE = 20
genepool = []
for i in range(0, GENSIZE):
    dna = [random.choice(string.printable[:-5]) for j in range(0, len(target))]
    fit = fitness(dna, target)
    candidate = {'dna': dna, 'fitness': fit }
    genepool.append(candidate)

def mutate(parent1, parent2):
    child_dna = parent1['dna'][:]

    # Mix both DNAs
    start = random.randint(0, len(parent2['dna']) - 1)
    stop = random.randint(0, len(parent2['dna']) - 1)
    if start > stop:
        stop, start = start, stop
    child_dna[start:stop] = parent2['dna'][start:stop]

    # Mutate one position
    charpos = random.randint(0, len(child_dna) - 1)
    child_dna[charpos] = chr(ord(child_dna[charpos]) + random.randint(-1,1))
    child_fitness = fitness(child_dna, target)
    return({'dna': child_dna, 'fitness': child_fitness})

def random_parent(genepool):
    wRndNr = random.random() * random.random() * (GENSIZE - 1)
    wRndNr = int(wRndNr)
    return(genepool[wRndNr])

i = 0
while True:
    i += 1
    genepool.sort(key=lambda candidate: candidate['fitness'])
    
    print "%5i %5i %14s" % (i, genepool[0]['fitness'], ''.join(genepool[0]['dna']))
    sleep(0.1)
    
    if genepool[0]['fitness'] == 0:
        break

    parent1 = random_parent(genepool)
    parent2 = random_parent(genepool)

    child = mutate(parent1, parent2)
    if child['fitness'] < genepool[-1]['fitness']:
        genepool[-1] = child
