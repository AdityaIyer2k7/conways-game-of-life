import pygame as pg
from Board import *
import time

squares = (100,100)
pixPerSquare = 700//squares[0]
b = Board(squares)

pg.display.init()
win = pg.display.set_mode(size=(pixPerSquare*squares[0], pixPerSquare*squares[1]))

white = (255,255,255)

running = True
tick = False
mouseDown = False
lastTick = 0
lastSave = [
    [0 for _ in range(squares[0])] for _ in range(squares[1])
]

while running:
    pg.display.flip()
    win.fill((0,0,0))
    if tick:
        b.boardTick()
        lastTick = time.time()
    for y in range(squares[1]):
        for x in range(squares[0]):
            if b.board[y][x] == 1:
                pg.draw.rect(win, white, pg.Rect(pixPerSquare*x, pixPerSquare*y, pixPerSquare, pixPerSquare))
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            x = event.pos[0]//pixPerSquare
            y = event.pos[1]//pixPerSquare
            b.board[y][x] = 1 - b.board[y][x]
        if event.type == pg.KEYDOWN:
            if event.key in [pg.K_SPACE, pg.K_RETURN]:
                tick = not tick
            elif event.key == pg.K_c:
                lastSave = b.board.copy()
            elif event.key == pg.K_v:
                b.board = lastSave.copy()
            elif event.key == pg.K_x:
                b.boardGen()
        if event.type == pg.QUIT:
            running = False
        
pg.quit()
