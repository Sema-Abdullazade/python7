import random
import math
def funk():
    i=0
    ededler_listi=[]
    while i<5:
        i+=1
        a=random.randrange(20,50)
        ededler_listi.append(a)
    print(f'Ededlerimiz: {ededler_listi}')
    kvadrat=[math.pow(i,2) for i in ededler_listi if i%2==0]
    print(f'Kvadratlari: {kvadrat}')

funk()