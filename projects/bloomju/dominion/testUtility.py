"""
Created on Sat Jan 18 2020

@author: Justin Bloom
"""

import Dominion
import random
from collections import defaultdict

def getBoxes(nV, boxSize):
    box = {}
    box["Woodcutter"] = [Dominion.Woodcutter()] * boxSize
    box["Smithy"] = [Dominion.Smithy()] * boxSize
    box["Laboratory"] = [Dominion.Laboratory()] * boxSize
    box["Village"] = [Dominion.Village()] * boxSize
    box["Festival"] = [Dominion.Festival()] * boxSize
    box["Market"] = [Dominion.Market()] * boxSize
    box["Chancellor"] = [Dominion.Chancellor()] * boxSize
    box["Workshop"] = [Dominion.Workshop()] * boxSize
    box["Moneylender"] = [Dominion.Moneylender()] * boxSize
    box["Chapel"] = [Dominion.Chapel()] * boxSize
    box["Cellar"] = [Dominion.Cellar()] * boxSize
    box["Remodel"] = [Dominion.Remodel()] * boxSize
    box["Adventurer"] = [Dominion.Adventurer()] * boxSize
    box["Feast"] = [Dominion.Feast()] * boxSize
    box["Mine"] = [Dominion.Mine()] * boxSize
    box["Library"] = [Dominion.Library()] * boxSize
    box["Gardens"] = [Dominion.Gardens()] * nV
    box["Moat"] = [Dominion.Moat()] * boxSize
    box["Council Room"] = [Dominion.Council_Room()] * boxSize
    box["Witch"] = [Dominion.Witch()] * boxSize
    box["Bureaucrat"] = [Dominion.Bureaucrat()] * boxSize
    box["Militia"] = [Dominion.Militia()] * boxSize
    box["Spy"] = [Dominion.Spy()] * boxSize
    box["Thief"] = [Dominion.Thief()] * boxSize
    box["Throne Room"] = [Dominion.Throne_Room()] * boxSize
    return box

def getSupplyOrder():
    supply_order = {0: ['Curse', 'Copper'], 2: ['Estate', 'Cellar', 'Chapel', 'Moat'],
                    3: ['Silver', 'Chancellor', 'Village', 'Woodcutter', 'Workshop'],
                    4: ['Gardens', 'Bureaucrat', 'Feast', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief',
                        'Throne Room'],
                    5: ['Duchy', 'Market', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Mine', 'Witch'],
                    6: ['Gold', 'Adventurer'], 8: ['Province']}
    return supply_order

def getSupply(nV, nC, box, player_names):
    # Pick 10 cards from box to be in the supply.
    supply = randomSupply(box)
    # The supply always has these cards
    supply["Copper"] = [Dominion.Copper()] * (60 - len(player_names) * 7)
    supply["Silver"] = [Dominion.Silver()] * 40
    supply["Gold"] = [Dominion.Gold()] * 30
    supply["Estate"] = [Dominion.Estate()] * nV
    supply["Duchy"] = [Dominion.Duchy()] * nV
    supply["Province"] = [Dominion.Province()] * nV
    supply["Curse"] = [Dominion.Curse()] * nC
    return supply


def randomSupply(box):
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]
    return defaultdict(list, [(k, box[k]) for k in random10])


def getPlayers(player_names):
    players = []
    for name in player_names:
        if name[0] == "*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0] == "^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    return players