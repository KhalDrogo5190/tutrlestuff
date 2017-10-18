from turtle import*

def draw_square(x,y,size,line, fill):
    penup()
    goto (x,y)
    pendown()

    points = 4
    turn = 90

    color(line,fill)

    begin_fill()
    for i in range(points):
        forward(size)
        right(turn)
    end_fill()   

def draw_circle(x,y,size,line, fill):
    penup()
    goto (x,y)
    pendown()

    points = 360
    turn = 1

    color(line,fill)

    begin_fill()
    for i in range(points):
        forward(size)
        right(turn)
    end_fill()

def draw_rectangle():
    print ("banana")
speed(100)
draw_square(-100,100,100, "black", "slate gray")
draw_square(-100,200,100, "black", "slate gray")
draw_square(0,100,100, "black", "slate gray")
draw_square(0,200,100, "black", "slate gray")
draw_square(100,100,100, "black", "slate gray")
draw_square(100,200,100, "black", "slate gray")
draw_square(200,100,100, "black", "slate gray")
draw_square(200,200,100, "black", "slate gray")
draw_square(300,100,100, "black", "slate gray")
draw_square(300,200,100, "black", "slate gray")
draw_circle(0,0,1,"medium spring green", "black")
draw_circle(300,0,1,"medium spring green", "black")
