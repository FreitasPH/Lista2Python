import turtle     # Tess becomes a traffic light.
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
	""" Draw a nice housing to hold the traffic lights """
	tess.pensize(3)
	tess.color("black", "darkgrey")
	tess.begin_fill()
	tess.forward(80)
	tess.left(90)
	tess.forward(200)
	tess.circle(40, 180)
	tess.forward(200)
	tess.left(90)
	tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

#A traffic light is a kind of state machine with three states,
#Green, Orange, Red. We number these states 0, 1, 2
#When the machine changes state, we change tess' position and
#her fillcolor.

# This variable holds the current state of the machine

state_num = 0
def advance_state_machine():
	global state_num
	if state_num == 0:		# Transition from state 0 to state 1
		tess.forward(70)
		tess.fillcolor("orange")
		state_num = 1
	elif state_num == 1:		# Transition from state 1 to state 2
		tess.forward(70)
		tess.fillcolor("red")
		state_num = 2
	else:				# Transition from state 2 to state 0
		tess.back(140)
		tess.fillcolor("green")
		state_num = 0

def state_machine_R():
	global state_num
	if state_num == 0:		# Transition from state 0 to state 2
		tess.forward(140)
	if state_num == 1:		# Transition from state 1 to state 2
		tess.forward(70)
	tess.fillcolor("red")
	state_num = 2

def state_machine_O():
	global state_num
	if state_num == 0:		# Transition from state 2 to state 1
		tess.forward(70)
	if state_num == 2:		# Transition from state 0 to state 1
		tess.back(70)
	tess.fillcolor("orange")
	state_num = 1

def state_machine_G():
	global state_num
	if state_num == 1:		# Transition from state 1 to state 0
		tess.back(70)
	if state_num == 2:		# Transition from state 2 to state 0
		tess.back(140)
	tess.fillcolor("green")
	state_num = 0

def increase_width():
	width = tess.shapesize()[2]
	if width < 20:
		tess.shapesize(outline=width+1)

def decrease_width():
	width = tess.shapesize()[2]
	if width > 1:
		tess.shapesize(outline=width-1)
		

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

# Bind the sectors of state.
wn.onkey(state_machine_R, "r")
wn.onkey(state_machine_O, "o")
wn.onkey(state_machine_G, "g")
wn.onkey(state_machine_R, "R")
wn.onkey(state_machine_O, "O")
wn.onkey(state_machine_G, "G")

# Bind the width changers.
wn.onkey(increase_width, "plus")
wn.onkey(decrease_width, "minus")

wn.listen()
wn.mainloop()
