'''
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
'''

import random

'''
def noppaa():

    while True:
        x = random.randint(1, 6)
        
        if x < 6:
            print(x)
            
        else:
            print(x)
            break

noppaa()
'''

def noppaa():

    x = 0
    while x != 6:
        x = random.randint(1, 6)
        print(x)

noppaa()
