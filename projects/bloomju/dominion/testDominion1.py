# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 2020

@author: Justin Bloom
"""

import Dominion
import testUtility
import random
from collections import defaultdict

# Get player names
player_names = ["Annie", "*Ben", "*Carla", "*Daniel", "*Ethan", "*Felicity"]

# number of curses and victory cards
if len(player_names) > 2:
    nV = 24
else:
    nV = 8
nC = -10 + 10 * len(player_names)


boxSize = 10 * (len(player_names) // 3)  #number of copies of each card from box

# Define box
box = testUtility.getBoxes(nV, boxSize)

supply_order = testUtility.getSupplyOrder()

# picks 10 cards from box to be used, and adds essential cards to supply
supply = testUtility.getSupply(nV, nC, box, player_names)

# initialize the trash
trash = []

# Construct the Player objects
players = testUtility.getPlayers(player_names)

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)