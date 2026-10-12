import turtle
import random

def tree(branch_len, t):
    m = random.randint(1, 10)
    n = random.randint(10, 20)
    if branch_len > 5:
        t.pensize(max(branch_len//10, 1))

        if branch_len < 20:
            t.color("green")
        else:
            t.color("brown")

        t.forward(branch_len)

        randomAngle = random.randint(15, 45)
        randomLen = random.randint(10, 15)

        t.right(randomAngle)
        tree(branch_len - randomLen, t)
        t.left(2 * randomAngle)
        tree(branch_len - randomLen, t)
        t.right(randomAngle)
        t.backward(branch_len)    

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    my_win.exitonclick()

main()
