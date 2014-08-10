# Import required modules
from time import *
from tkinter import *

# Initialise the window
window = Tk()
window.title("Alien")
c = Canvas(window, height=300, width=400)
c.pack()

# Draw the alien
body = c.create_oval(100, 150, 300, 250, fill='green')
eye = c.create_oval(170, 70, 230, 130, fill='white')
eyeball = c.create_oval(190, 90, 210, 110, fill='black')
mouth = c.create_oval(150, 220, 250, 240, fill='red')
neck = c.create_line(200, 150, 200, 130)
hat = c.create_polygon(180, 75, 220, 75, 200, 20, fill='blue')

# Function to open mouth
def mouth_open():
    c.itemconfig(mouth, fill='black')

# Function to close mouth
def mouth_close():
    c.itemconfig(mouth, fill="red")

# Function to blink
def blink(event):	# Parameter for events
    c.itemconfig(eye, fill='green')
    c.itemconfig(eyeball, state=HIDDEN)

# Function to unblink
def unblink(event):	# Parameter for events
    c.itemconfig(eye, fill='white')
    c.itemconfig(eyeball, state=NORMAL)
words = c.create_text(200, 280, text='I am an Alien!')

# Fucntion to make hat dissapear
def steal_hat():
    c.itemconfig(hat, state=HIDDEN)
    c.itemconfig(words, text='Give my hat back!')
    window.attributes('-topmost', 1)

# Function to make alien burp
def burp(event):	# Parameter for events
    mouth_open()
    c.itemconfig(words, text='Burp!')

# Fucntion to unburp
def unburp(event):	# Parameter for events
    mouth_close()
    c.itemconfig(words, text="I am an Alien!")

# Bind functions to events
c.bind_all('<KeyPress-b>', unburp)
c.bind_all('<Button-1>', burp)
c.bind_all('<KeyPress-a>', blink)
c.bind_all('<KeyPress-z>', unblink)

# Eye control function
def eye_control(event):
    key = event.keysym
    if key == "Up":
        c.move(eyeball, 0, -1)
    elif key == "Down":
        c.move(eyeball, 0, 1)
    elif key == "Left":
        c.move(eyeball, -1, 0)
    elif key == "Right":
        c.move(eyeball, 1, 0)

# Bind eye_control function to keypress event
c.bind_all('<Key>', eye_control)

# Function to make the alien blink
def blin():
    c.itemconfig(eye, fill='green')
    c.itemconfig(eyeball, state=HIDDEN)

# Function to make alien unblink
def unblin():
    c.itemconfig(eye, fill='white')
    c.itemconfig(eyeball, state=NORMAL)



   
    



                 

