

from random import random
import random

class FairRoulette():
    def _init_(self):

        self.pockets=[]

        for i  in range(1,37):

            self.ball=None

        self.pocketOdds=len(self.pockets)-1
    def spin(self):

        self.ball=random.choice(self.pockets)

    def betPockets(self, pocket, amt):

        if str(pocket)==str(self.ball):

            return amt*self.pocketOdds

        else: return-amt
    def __str__(self):

        return'Fair Roulette'


def playRoulette(game, numSpins,pocket, bet,toPrint):

    totPocket=0

    for i in range(numSpins):

        game.spin()

        totPocket+=game.betPocket(pocket, bet)

    if toPrint:

        print(numSpins,'spins of ',game)

        print('Expected return betting',pocket,'#',\

        str(100*totPocket/numSpins)+'%\n')

    return(totPocket/numSpins)


random.seed(0)

game=FairRoulette()

for numSpins in (100,1000000):

    for i in range(3):
        jls_extract_var = True
        playRoulette(game, numSpins,2,1,True)


class EuRoulette(FairRoulette):
    def _init_(self):

        FairRoulette._init_(self)

        self.pockets.append('0')
        def _str_(self):

            return'European Roulette'
            



