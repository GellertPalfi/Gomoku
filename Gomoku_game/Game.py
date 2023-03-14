import pygame
from Aiplayer import Aiplayer
from Board import Board

from Gomoku import Gomoku

pygame.init()
# aiplayer = Aiplayer()
gomoku = Gomoku()

gomoku.play()
# Done! Time to quit.
pygame.quit()
