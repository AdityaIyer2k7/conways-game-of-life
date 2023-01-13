from Board import *

b = Board((20,20))

print(b)

running = True
while running:
    cmd = input("Command 'Enter' to play, {x y v} to modify, x to quit: ")
    try:
        if cmd == "": b.boardTick()
        elif cmd == "x": running = False
        else:
            x,y,v = cmd.split()
            x = int(x)
            y = int(y)
            v = int(v)
            b.board[y][x] = v
    except Exception as e:
        print(e)
    print(b)
    
