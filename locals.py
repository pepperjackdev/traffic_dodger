import pygame

""" Constants """
MARGIN = 40

""" Shared variables """
_SCORE = 0

def get_score():
    return _SCORE

def inc_score():
    global _SCORE
    _SCORE += 1