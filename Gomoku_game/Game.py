import pygame
from Board import Board

from Gomoku import Gomoku

pygame.init()

running = True
gomoku = Gomoku()
board = Board()


gomoku.play()
# Done! Time to quit.
pygame.quit()
