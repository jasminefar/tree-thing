import turtle

class FractalTreeDrawer:
    def __init__(self, initial_length=300, angle=20, reduction_factor=0.9, min_length=5, speed=1, thickness=10):
        """
        Initialize the FractalTreeDrawer with initial parameters.
        
        initial_length: The starting length of the tree trunk.
        angle: The angle between branches.
        reduction_factor: The factor by which each branch length is reduced.
        min_length: The minimum length of a branch before stopping recursion.
        speed: The drawing speed of the turtle.
        thickness: The initial thickness of the trunk.
        """
        self.initial_length = initial_length
        self.angle = angle
        self.reduction_factor = reduction_factor
        self.min_length = min_length
        self.speed = speed
        self.thickness = thickness
        self.t = turtle.Turtle()
        self.t.speed(speed)
        self.t.left(90)  # Point the turtle upwards
    
    def draw_tree(self, length, thickness):
        """
        Recursively draw the fractal tree.
        
        length: The current length of the branch.
        thickness: The thickness of the current branch.
        """
        if length > self.min_length:
            self.t.pensize(thickness)
            self.t.forward(length)
            self.t.left(self.angle)
            self.draw_tree(length * self.reduction_factor, thickness * self.reduction_factor)
            self.t.right(2 * self.angle)
            self.draw_tree(length * self.reduction_factor, thickness * self.reduction_factor)
            self.t.left(self.angle)
            self.t.backward(length)
    
    def add_ground(self):
        """Draw a simple ground for the tree."""
        self.t.penup()
        self.t.goto(-400, -300)
        self.t.pendown()
        self.t.forward(800)
    
    def start_drawing(self):
        """Start the drawing process."""
        turtle.bgcolor("sky blue")
        self.add_ground()
        self.t.penup()
        self.t.goto(0, -300)  # Position the turtle at the bottom center
        self.t.pendown()
        self.draw_tree(self.initial_length, self.thickness)
        turtle.done()

    def set_color(self, branch_color="brown", leaf_color="green"):
        """
        Set the color for the branches and leaves.
        
        branch_color: The color of the branches.
        leaf_color: The color of the leaves.
        """
        self.branch_color = branch_color
        self.leaf_color = leaf_color

    def draw_leaf(self):
        """Draw a simple leaf at the end of each branch."""
        self.t.color(self.leaf_color)
        self.t.begin_fill()
        self.t.circle(3)
        self.t.end_fill()
        self.t.color(self.branch_color)

    def draw_tree_with_leaves(self, length, thickness):
        """
        Recursively draw the fractal tree with leaves.
        
        length: The current length of the branch.
        thickness: The thickness of the current branch.
        """
        if length > self.min_length:
            self.t.pensize(thickness)
            self.t.forward(length)
            self.t.left(self.angle)
            self.draw_tree_with_leaves(length * self.reduction_factor, thickness * self.reduction_factor)
            self.t.right(2 * self.angle)
            self.draw_tree_with_leaves(length * self.reduction_factor, thickness * self.reduction_factor)
            self.t.left(self.angle)
            self.t.backward(length)
        else:
            self.draw_leaf()

    def start_drawing_with_leaves(self):
        """Start the drawing process with leaves."""
        self.set_color()
        turtle.bgcolor("sky blue")
        self.add_ground()
        self.t.penup()
        self.t.goto(0, -300)  # Position the turtle at the bottom center
        self.t.pendown()
        self.draw_tree_with_leaves(self.initial_length, self.thickness)
        turtle.done()

# Create an instance of FractalTreeDrawer with parameters to extend drawing time and start drawing
tree = FractalTreeDrawer(initial_length=300, angle=25, reduction_factor=0.9, min_length=2, speed=1, thickness=10)
tree.start_drawing_with_leaves()
