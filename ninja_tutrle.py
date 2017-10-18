import random
from turtle import*
Leo = Turtle()
Mikey = Turtle()
Raph = Turtle()
Don = Turtle()

Leo.shape("turtle")
Leo.color("CadetBlue2")

Mikey.shape("turtle")
Mikey.color("gold")

Raph.shape("turtle")
Raph.color("firebrick1")

Don.shape("turtle")
Don.color("dark violet")

all_turtles = [Leo, Mikey, Raph, Don]

while True:
    for t in all_turtles:
        rand_dir = random.randomint(-20,20)
        rand_dis = random.randomint(5,100)

        t.right(rand_dir)
        t.forward(rand_dis)
