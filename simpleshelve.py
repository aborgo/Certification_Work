"""
Stores sports scores in a shelf.
"""

import shelve
import os

def storescore(player,score):
    shelf = shelve.open(os.path.join(os.getcwd(), "scorestore.shlf"))
    if not shelf.get(player):
        shelf[player] = score
    if shelf.get(player):
        if score > shelf[player]:
            shelf[player] = score
    highscore = shelf[player]
    shelf.close()
    return highscore
