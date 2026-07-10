import turtle as t
import random
import time

# Game Variables
d = 0.1
s = 0
hs = 0
run = True

# Screen Setup
sc = t.Screen()
sc.title("Snake Game")
sc.bgcolor("#add8e6")
sc.setup(width=600, height=600)
sc.tracer(0)

# Snake Head
h = t.Turtle()
h.shape("square")
h.color("white")
h.penup()
h.goto(0, 0)
h.direction = "Stop"

# Food
f = t.Turtle()
f.shape(random.choice(["circle", "square", "triangle"]))
f.color(random.choice(["red", "green", "black"]))
f.penup()
f.goto(0, 100)

# Scoreboard
p = t.Turtle()
p.hideturtle()
p.penup()
p.goto(0, 250)
p.write("Score : 0  High Score : 0", align="center", font=("Candara", 24, "bold"))

# Movement Functions
def up():
    if h.direction != "down":
        h.direction = "up"

def down():
    if h.direction != "up":
        h.direction = "down"

def left():
    if h.direction != "right":
        h.direction = "left"

def right():
    if h.direction != "left":
        h.direction = "right"

def move():

    if h.direction == "up":
        h.sety(h.ycor() + 20)

    elif h.direction == "down":
        h.sety(h.ycor() - 20)

    elif h.direction == "left":
        h.setx(h.xcor() - 20)

    elif h.direction == "right":
        h.setx(h.xcor() + 20)

# Keyboard Controls
sc.listen()

sc.onkeypress(up, "Up")
sc.onkeypress(down, "Down")
sc.onkeypress(left, "Left")
sc.onkeypress(right, "Right")

# Snake Body
seg = []

# Main Game Loop
while run:
    try:
        sc.update()

        # Wall Collision
        if abs(h.xcor()) > 290 or abs(h.ycor()) > 290:
            time.sleep(1)
            h.goto(0, 0)
            h.direction = "Stop"

            for segment in seg:
                segment.goto(1000, 1000)
            seg.clear()

            s = 0
            d = 0.1

            p.clear()
            p.write(f"Score : {s}  High Score : {hs}",
                    align="center",
                    font=("Candara", 24, "bold"))

        # Food Collision
        if h.distance(f) < 20:
            f.goto(random.randint(-270, 270), random.randint(-270, 270))

            new_seg = t.Turtle()
            new_seg.shape("square")
            new_seg.color("orange")
            new_seg.penup()

            seg.append(new_seg)

            d -= 0.001
            s += 10

            if s > hs:
                hs = s

            p.clear()
            p.write(f"Score : {s}  High Score : {hs}",
                    align="center",
                    font=("Candara", 24, "bold"))

        # Move Body
        for i in range(len(seg) - 1, 0, -1):
            x = seg[i - 1].xcor()
            y = seg[i - 1].ycor()
            seg[i].goto(x, y)

        if len(seg) > 0:
            seg[0].goto(h.xcor(), h.ycor())

        # Move Snake
        move()

        # Self Collision
        for segment in seg:
            if segment.distance(h) < 20:
                time.sleep(1)

                h.goto(0, 0)
                h.direction = "Stop"

                for segment in seg:
                    segment.goto(1000, 1000)

                seg.clear()

                s = 0
                d = 0.1

                p.clear()
                p.write(f"Score : {s}  High Score : {hs}",
                        align="center",
                        font=("Candara", 24, "bold"))

        time.sleep(d)

    except t.Terminator:
        run = False