# Program to convert celsius to fahrenheit using a simple GUI.

from graphics import *
def main():
    win = GraphWin("Celsius Converter", 300, 200)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # Draw interface
    Text(Point(1,3), " Celsius Temp:").draw(win)
    Text(Point(1,1), "Fahrenheit Temp:").draw(win)
    input = Entry(Point(2,3), 5)
    input.setText("0.0")
    input.draw(win)
    output = Text(Point(2,1),"")
    output.draw(win)
    button = Text(Point(1.5,2.0), "Convert")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)

    win.getMouse()

    celsius = eval(input.getText())
    fahrenheit = 9.0/5.0 * celsius + 32

    output.setText(fahrenheit)
    button.setText("Quit")
    # click close
    win.getMouse()
    win.close()
    
