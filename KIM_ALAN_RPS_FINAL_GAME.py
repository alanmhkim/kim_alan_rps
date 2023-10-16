# The turtle module is a lightweight graphics library for teaching python
import turtle
from turtle import *
from random import randint
choices = ["rock", "paper", "scissors"]
cpuchoice = choices[randint(0,2)]

#define number for rps art - when printing art in terminal we need a number to access the value in the dictionary.
if cpuchoice == "rock":
    imagecpuchoice = 0
elif cpuchoice == "paper":
    imagecpuchoice = 1
elif cpuchoice == "scissors":
    imagecpuchoice = 2

# The os module allows us to access the current directory in order to access assets
import os
 
# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400
 
# setting variables for image length and height for hitbox determination
rock_w = 154
rock_h = 170
paper_w = 241
paper_h = 157
scissors_w = 256
scissors_h = 170
 

#rock paper scissors ASCII art

#rock art
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

#paper art
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

#scissor art
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
#Dictionary of the rps game images - user inputs are used to retrive and print art using the dictionary and its indexes.
game_images = [rock, paper, scissors]


# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')
 
# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="light green")
 
# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
cpu_rock = os.path.join(images_folder, 'cpu_rock.gif')
 
paper_image = os.path.join(images_folder, 'paper.gif')
cpu_paper = os.path.join(images_folder, 'cpu_paper.gif')
 
scissors_image = os.path.join(images_folder, 'scissors.gif')
cpu_scissors = os.path.join(images_folder, 'cpu_scissors.gif')
# instantiate (create an instance of) the Turtle class for the rock, paper, and scissors.
rock_instance = turtle.Turtle()
cpu_rock_instance = turtle.Turtle()
cpu_rock_instance.hideturtle()
cpu_rock_instance.penup()
 
paper_instance = turtle.Turtle()
cpu_paper_instance = turtle.Turtle()
cpu_paper_instance.hideturtle()
 
scissors_instance = turtle.Turtle()
cpu_scissors_instance = turtle.Turtle()
cpu_scissors_instance.hideturtle()
#we hide the turtle to hide the icon in the code.
 
screen.addshape(rock_image)
screen.addshape(paper_image)
screen.addshape(scissors_image)
screen.addshape(cpu_rock)
screen.addshape(cpu_paper)
screen.addshape(cpu_scissors)
# attach the rock_image to the rock_instance
rock_instance.shape(rock_image)
paper_instance.shape(paper_image)
scissors_instance.shape(scissors_image)
cpu_rock_instance.shape(cpu_rock)
 
cpu_paper_instance.shape(cpu_paper)
cpu_paper_instance.penup()
 
cpu_scissors_instance.shape(cpu_scissors)
cpu_scissors_instance.hideturtle()
cpu_scissors_instance.penup()

#defining the position of rock, paper, and scissors when running first. 
rock_pos_x = -300
rock_pos_y = 0
paper_pos_x = 0
paper_pos_y = 0
scissors_pos_x = 300
scissors_pos_y = 0
rock_instance.penup()
paper_instance.penup()
scissors_instance.penup()
 
#setting nthe positions of rock, paper, and scissors and moving them to the location when running.
rock_instance.setpos(rock_pos_x,rock_pos_y)
paper_instance.setpos(paper_pos_x, paper_pos_y)
scissors_instance.setpos(scissors_pos_x, scissors_pos_y)

#write text function - writes text in the window
def write_text(message, x, y):
    text = turtle.Turtle()
    text.color('black')
    text.penup()
    text.setpos(x,y)
    text.hideturtle()
    text.write(message, False, "center", ("Arial", 22, "bold"))

#opening text - welcome text
write_text("Welcome to Rock, Scissors, Paper!", 0, 150)

# remove the pen option from the rock_instance so it doesn't draw lines when moved

 
#defining when mouse collides with an image or not
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False
 
userchoice = "nothing"
 
# defining a function where if we click the image on the screen we send a message to terminal to correlate.
def mouse_pos(x, y):
    #when the mouse collides on rock
    if collide(x,y,rock_instance,rock_w,rock_h):
        #setting user choice to rock and imageuserchoice to 0 to print in terminal the choice and art
        userchoice = "rock"
        imageuserchoice = 0
        print(f"Your Choice: {userchoice} {game_images[imageuserchoice]}\nComputer choice: {cpuchoice} {game_images[imagecpuchoice]}")
        paper_instance.hideturtle()
        scissors_instance.hideturtle()
        #depending on the cpu choice, it shows the cpu turtle accordingly. WIN/LOSE/TIE
        if cpuchoice == "paper":
            print("You lost")
            cpu_paper_instance.showturtle()
            cpu_paper_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("Womp Womp, You Lost!", 0, 0)
        elif cpuchoice == "rock":
            print("You tie")
            cpu_rock_instance.showturtle()
            cpu_rock_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("Wow! You Tied!", 0, 0)
        elif cpuchoice == "scissors":
            print("You win")
            cpu_scissors_instance.showturtle()
            cpu_scissors_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("HOORAY!!! You Win!", 0, 0)
    elif collide(x,y,paper_instance,paper_w,paper_h):
        #setting user choice to paper and imageuserchoice to 1 to print in terminal the choice and art
        rock_instance.hideturtle()
        scissors_instance.hideturtle()
        paper_instance.setpos(rock_pos_x, rock_pos_y)
        userchoice = "paper"
        imageuserchoice = 1
        print(f"Your Choice: {userchoice} {game_images[imageuserchoice]}\nComputer choice: {cpuchoice} {game_images[imagecpuchoice]}")
        #depending on the cpu choice, it shows the cpu turtle accordingly. WIN/LOSE/TIE
        if cpuchoice == "paper":
            print("You tie")
            cpu_paper_instance.showturtle()
            cpu_paper_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("Wow! You Tied!", 0, 0)
        elif cpuchoice == "rock":
            print("You win")
            cpu_rock_instance.showturtle()
            cpu_rock_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("HOORAY!!! You Win!", 0, 0)
        elif cpuchoice == "scissors":
            print("You lose")
            cpu_scissors_instance.showturtle()
            cpu_scissors_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("Womp Womp, You Lost!", 0, 0)
    elif collide(x,y,scissors_instance,scissors_w,scissors_h):
        #setting user choice to scissors and imageuserchoice to 2 to print in terminal the choice and art
        paper_instance.hideturtle()
        rock_instance.hideturtle()
        scissors_instance.setpos(rock_pos_x, rock_pos_y)
        userchoice = "scissors"
        imageuserchoice = 2
        print(f"Your Choice: {userchoice} {game_images[imageuserchoice]}\nComputer choice: {cpuchoice} {game_images[imagecpuchoice]}")
        #depending on the cpu choice, it shows the cpu turtle accordingly. WIN/LOSE/TIE
        if cpuchoice == "paper":
            print("You win")
            cpu_paper_instance.showturtle()
            cpu_paper_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("HOORAY!!! You Win!", 0, 0)
        elif cpuchoice == "rock":
            print("You lost")
            cpu_rock_instance.showturtle()
            cpu_rock_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("Womp Womp, You Lost!", 0, 0)
        elif cpuchoice == "scissors":
            print("You tie")
            cpu_scissors_instance.showturtle()
            cpu_scissors_instance.setpos(scissors_pos_x, scissors_pos_y)
            write_text("Wow! You Tied!", 0, 0)
    else:
        #if the user does not click within the hitbox of rock, scissors, or paper images, then ask the user to click on somehting and assign that the user choice is nothing.
        userchoice = "nothing"
        print("choose something fool!")
        
#screen module onclick - action that will be triggered when the user clicks on the mouse
screen.onclick(mouse_pos)

# have the turtle module 'listen' for when keys are pressed
turtle.listen()
 
# when the turtle 'x' key is pressed then quit turtle
turtle.done()