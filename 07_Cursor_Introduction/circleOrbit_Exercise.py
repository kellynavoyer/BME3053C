try:
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import numpy as np
except ImportError as e:
    print(f"Error: {e}")
    print("It seems that matplotlib is not installed. Please install it using pip:")
    print("pip install matplotlib")
    exit(1)

# Set up the figure and axis
fig, ax = plt.subplots()

# Create the box
box = plt.Rectangle((-0.5, -0.5), 1, 1, fill=False)
ax.add_patch(box)

# Create the orbiting circle
circle = plt.Circle((0, 0), 0.1, fill=False)
ax.add_patch(circle)

# Set the axis limits
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

# Animation function
def animate(frame):
    # Calculate new position of the circle
    theta = np.radians(frame)
    x = 1.5 * np.cos(theta)
    y = 1.5 * np.sin(theta)
    
    # Update circle position
    circle.center = (x, y)
    
    return circle,

try:
    # Create the animation
    anim = animation.FuncAnimation(fig, animate, frames=360, interval=20, blit=True)

    # Add title
    plt.title("Circle Orbiting Around a Box")

    # Show the animation
    plt.show()
except Exception as e:
    print(f"An error occurred while running the animation: {e}")
