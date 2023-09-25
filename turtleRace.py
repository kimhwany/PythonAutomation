import turtle as t
import random
import time

def main():
    scr = t.Screen()
    scr.setup(width=500, height=500)
    user_input = scr.textinput(title="Which Turtle do you want to bet on? ", prompt="Enter it's color below (Red, Yellow, Green, Blue)")
    turtle_colors = ["Red", "Yellow", "Green", "Blue"]
    RaceRunning = False
    Runners = []
    pos = -100

    # for each and every turtle
    for i in range(len(turtle_colors)):
        NewTurtle = t.Turtle()
        NewTurtle.shape("turtle")
        NewTurtle.penup()
        NewTurtle.color(turtle_colors[i])
        NewTurtle.goto(x=-250, y=pos)
        pos += 50
        Runners.append(NewTurtle)

    if user_input: RaceRunning = True

    while RaceRunning:
        for runner in Runners:
            if runner.xcor() > 230:
                winner = runner.pencolor()
                RaceRunning = False
                show = t.Turtle()
                show.hideturtle()
                show.penup()
                show.goto(-200, -150)
                show.color("red")

                if winner.lower() == user_input.lower():
                    show.write("Your turtle won!")
                else:
                    show.write(f"Sorr! Your turtle lost, the winner was {winner} turtle!")
            runner.forward(random.randint(0, 10))
    scr.exitonclick()


if __name__ == '__main__':
    main()