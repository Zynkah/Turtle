import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0: # Base Case
        myTurtle.forward(lineLen) # state change to move towards base case
        myTurtle.right(90)  # how many degrees to turn right at the end of the line length
        drawSpiral(myTurtle, lineLen-15)  # change the width between the lines, also the recursive part of the function


drawSpiral(myTurtle, 300)
myWin.exitonclick() # clicking on screen when animation is done will execute an exit
