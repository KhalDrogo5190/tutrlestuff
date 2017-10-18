from turtle import *

def draw_star(x, y, points, size, line, fill):
    penup ()
    goto(x,y)
    pendown ()

    turn = 180 - (360/points)

    color(line, fill)

    begin_fill()
    for i in range(points): 
        forward(size)
        right(turn)
    end_fill()

speed(100)
draw_star(0, 0, 6, 100, "red", "purple3")
draw_star(-100, 0, 10, 150, "cyan", "sea green")
draw_star(-200, 0, 12, 200, "blue", "yellow")
draw_star(-300, 0, 36, 250, "yellow", "blue")
draw_star(-400, 0, 90, 300, "purple3", "orange")
draw_star(-500, 0, 180, 350, "orange", "indigo")
draw_star(-600, 0, 360, 400, "purple", "red")
done()

