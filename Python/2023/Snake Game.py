from tkinter import *
from tkinter import simpledialog
import random

# Initialize the Tkinter window
window = Tk()
window.title("EMP Snake Game")
window.resizable(True, True)

# Prompt for user_name and continuous using simpledialog
user_name = simpledialog.askstring("Input", "What is your name?", parent=window)
continuous = simpledialog.askstring("Input", "Do you want to play in repeat mode or normal mode (R/N):", parent=window).lower()

# Close the prompt window
window.destroy()

# Initialize the main game window
window = Tk()
window.title("EMP Snake Game")
window.resizable(True, True)


# Constants for the game
GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 100
SPACE_SIZE = 50
BODY_PART = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "blue"
BACKGROUND_COLOR = "grey"

# Snake class to represent the player-controlled snake


class Snake():
    def __init__(self, canvas):
        """
        Initialize the Snake object.

        Parameters:
        - canvas: The canvas on which the snake will be drawn.
        """
        self.body_size = BODY_PART
        self.coordinates = []
        self.squares = []

        # Initialize the snake's body coordinates
        for _ in range(0, BODY_PART):
            self.coordinates.append([0, 0])

        # Create rectangles for each body part of the snake
        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)

# Food class to represent the food that the snake can eat


class Food():
    def __init__(self, canvas):
        """
        Initialize the Food object.

        Parameters:
        - canvas: The canvas on which the food will be spawned.
        """
        self.canvas = canvas
        self.spawn_food()

    def spawn_food(self):
        """
        Spawn food at a random location on the canvas.
        """
        x = random.randint(0, GAME_WIDTH // SPACE_SIZE - 1) * SPACE_SIZE
        y = random.randint(0, GAME_HEIGHT // SPACE_SIZE - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        self.canvas.create_oval(x, y, x + SPACE_SIZE,
                                y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")


# Function to handle the game logic for each turn
def next_turn(snake, food):
    """
    Move the snake in the current direction and handle game logic for each turn.

    Parameters:
    - snake: Snake object representing the snake on the canvas.
    - food: Food object representing the food that the snake can eat.
    """
    global direction, game_after_id
    x, y = snake.coordinates[0]

    # Move the snake's head based on the current direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Update the snake's coordinates
    snake.coordinates.insert(0, (x, y))

    # Check if the snake has eaten the food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.configure(text="Score:{}".format(score))
        canvas.delete("food")
        food.spawn_food()
    else:
        # If not eaten, remove the last body part of the snake
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Create a new rectangle for the snake's head
    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    # Check for collisions with walls or itself
    if check_collision(snake):
        if continuous == "r":
            reset_game()
        elif continuous == "n":
            game_over()
    else:
        # Schedule the next turn after a delay (SPEED)
        game_after_id = window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    """
    Change the direction of the snake based on user input.

    Parameters:
    - new_direction: The new direction to set for the snake.
    """
    global direction

    # Update the direction if it is a valid change
    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_collision(snake):
    """
    Check for collisions with walls or itself.

    Parameters:
    - snake: Snake object representing the snake on the canvas.

    Returns:
    - True if a collision is detected, False otherwise.
    """
    x, y = snake.coordinates[0]

    # Check for collisions with walls
    if x < 0 or x > GAME_WIDTH:
        return True
    elif y < 0 or y > GAME_HEIGHT:
        return True

    # Check for collisions with itself
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False


# Function to handle the end of the game
def game_over():
    """
    End the game, display the final score, and write the score to a file.

    The function writes the user's name and final score to a "score.txt" file,
    clears the canvas, and displays a "Game Over" message in red.

    Note: Assumes the global variables user_name and score are defined.

    Returns:
    None
    """
    with open("score.txt", "a") as file:
        file.write(f"{user_name} score: {score} in normal mode\n")
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('Helvetica', 40, 'bold'), text="Game Over", fill="red", tag="gameover")


def reset_game():
    """
    Reset the game, display the final score, and write the score to a file.

    The function writes the user's name and final score to a "score.txt" file,
    clears the canvas, and displays a "Game Over" message in red. It then waits
    for 3 seconds before calling the perform_reset function to reset the game.

    Note: Assumes the global variables user_name, score, direction, canvas, and window are defined.

    Returns:
    None
    """
    global score, direction, game_after_id
    with open("score.txt", "a") as file:
        file.write(f"{user_name} score: {score} in repeat mode\n")
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('Helvetica', 40, 'bold'), text="Game Over", fill="red", tag="gameover")

    # Wait for 3 seconds (3000 milliseconds) before resetting the game
    window.after(3000, perform_reset)


def perform_reset():
    """
    Perform the reset of the game after waiting for 3 seconds.

    The function resets the score, direction, and canvas. It creates a new snake
    and food objects and starts the game loop by calling the next_turn function.

    Note: Assumes the global variables score, direction, label, canvas, Snake, Food, and next_turn are defined.

    Returns:
    None
    """
    global score, direction
    # Reset the score and direction
    score = 0
    direction = 'down'
    label.configure(text="Score:{}".format(score))

    # Delete all elements on the canvas
    canvas.delete(ALL)

    # Create a new snake and food
    snake = Snake(canvas)
    food = Food(canvas)
    # Start the game loop
    next_turn(snake, food)


# Initialize the Tkinter window
window = Tk()
window.title("EMP Snake Game")
window.resizable(True, True)

# Initial settings and UI elements
score = 0
direction = 'down'


# Display the score label
label = Label(window, text="Score:{}".format(
    score), font=('Helvetica', 40, 'bold'))
label.pack()

# Create the canvas for the game
canvas = Canvas(window, bg=BACKGROUND_COLOR,
                width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

# Center the window on the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width - GAME_WIDTH) / 2)
y = int((screen_height - GAME_HEIGHT) / 2)
window.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}+{x}+{y}")

# Bind arrow keys to change the direction of the snake
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<r>', lambda event: reset_game())

# Initialize the snake and food objects, and start the game loop
snake = Snake(canvas)
food = Food(canvas)
next_turn(snake, food)

# Start the Tkinter event loop
window.mainloop()
