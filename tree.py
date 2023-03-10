import turtle

def tree(branchLen, thickness, t):
    if branchLen > 8 and thickness > 0:
        t.pensize(thickness)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-16, thickness-2, t) # recursive call to the right
        t.left(40) # add an additional 20 degrees to undo the original 20 to the right
        tree(branchLen-14, thickness-2, t) # recursive call to the left
        t.right(20)
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.shape('turtle') # make the pointer a turtle!
    t.shapesize(2) # make turtle bigger
    tree(100, 12, t)
    myWin.exitonclick()

main()