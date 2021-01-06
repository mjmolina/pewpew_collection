import pew


pew.init()
screen = pew.Pix()
p = screen.pixel
background = pew.Pix.from_iter((
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
))

def posicion1(x, offset=0):

    # columna 0 y 7
    for y in range(0+offset, 7+offset):
        p(x, y, 3)
        p(x+7, y, 3)

    # columna 1 y 6
    p(x+1, 3+offset, 3)
    p(x+6, 3+offset, 3)

    # columna 2 y 5
    for y in range(2+offset, 5+offset):
        p(x+2, y, 3)
        p(x+5, y, 3)

    # columna 3 y 4
    for y in range(1+offset,6+offset):
        p(x+3, y, 3)
        p(x+4, y, 3)

    p(x+4, 7+offset, 3)
    p(x+3, 9+offset, 3)

x = 0
o = -7
while True:
    keys = pew.keys()
    screen.blit(background)

    if o > 8:
        o = -7
    
    posicion1(x, offset=o)
    pew.show(screen)
    screen.blit(background)
    pew.tick(0.2)
    o += 1
