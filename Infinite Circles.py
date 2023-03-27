import turtle

# Create a turtle object
t = turtle.Turtle()

# Define a function to draw a circle
def draw_circle(radius):
    t.circle(radius)

# Set the initial radius of the circle
radius = 10

# Loop to draw an infinite number of circles
while True:
    draw_circle(radius)
    radius += 10  # Increase the radius for the next circle
    t.clear()     # Clear the previous circle
