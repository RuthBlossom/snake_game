from turtle import Turtle

# tuples representing the initial positions of the snake segments.
# constants are named with all caps

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# extract move distance as const
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

	# And remember, we're going to need to use self when we're working within a class.
	# An empty list segments is created to store the Turtle objects representing the snake segments.
	def __init__(self):
		#creating attributes
		#look at positioning of the code. if you had the head before create_snake it is empty
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]

	# create method
	# Create three white square 'turtles'
	# Creating Initial Snake Segments:
	# change starting_positions into const.
	def create_snake(self):
		for positions in STARTING_POSITIONS:
			new_segment = Turtle(shape="square")
			new_segment.color("white")
			new_segment.penup()
			new_segment.goto(positions)
			self.segments.append(new_segment)
			# in order to refer to our attribute segments, we have to say self.segments

	# A loop creates three white square turtle segments at the specified starting positions. These segments are added to the segments list.
	def move(self):
		# Python doesn't take arguments
		# for seg_num in range(start=2, stop=0, step=-1):
		# for seg_num in range(start=len(segments) -1, stop=0, step=-1):
		# This loop iterates over the snake segments in reverse order (from the last segment to the first).
		# It updates the position of each segment to the position of the segment ahead of it. This creates a cascading effect, where each segment follows the one in front of it.
		for seg_num in range(len(self.segments) - 1, 0, -1):
			new_x = self.segments[seg_num - 1].xcor()
			new_y = self.segments[seg_num - 1].ycor()
			self.segments[seg_num].goto(new_x, new_y)
		# The head of the snake (the first segment in the list) moves forward by 20 units in the direction it is facing.
		self.head.forward(MOVE_DISTANCE)
		# The main game loop runs while game_is_on is True. It updates the screen and introduces a small delay (time.sleep(0.1)) to control the speed of the snake.

#heading as a method
	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)


	#create a separate attribute for head of snake as it will be used a number of times.