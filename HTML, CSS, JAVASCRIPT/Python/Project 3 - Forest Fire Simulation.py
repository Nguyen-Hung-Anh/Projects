'''
Write a program to simulate a forest fire. The program should be a graphical one, 
which allows the program's user to observe the way fire spreads, in addition to 
automatically computing statistics about the fire, including how much of the forest 
was destroyed, and how long the fire burned. The program should allow the user 
to enter different probabilities of fire spreading, so that they can explore the relationship 
between this probability and the fire's behavior.
'''


# Import necessary modules
from graphics import *
from tree import Tree
from button import Button
import random
import time

# GLOBAL VARIABLES FOR WIDTH AND HEIGHT
TREE_WIDTH = 29
TREE_HEIGHT = 29

# Function to draw the entire forest on the graphics window
def draw_forest(forest, win):
    # Loop through each row and tree, drawing them on the window
    for row in forest:
        for tree in row:
            tree.draw(win)

# Function to convert text input to a probability value (between 0 and 1)
def convert_text_to_probability(text):
    try:
        # Convert text to a float
        res = float(text)
        # Check if the float is within the valid probability range (0 to 1)
        if 0 <= res <= 1:
            return res
        return None  # Return None if the probability is invalid
    except ValueError:
        return None  # Return None if conversion to float fails

# Function to check if any tree in the forest is on fire
def forest_on_fire(forest):
    # Loop through each row and tree, checking if it's on fire
    for row in forest:
        for tree in row:
            if tree.is_on_fire():
                return True
    return False

# Function to set trees on fire based on their burn level
def set_on_fire(forest, win):
    # Loop through each row and tree, setting trees on fire if their burn level is greater than 0
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            if forest[i][j].burn_level > 0:
                forest[i][j].burn_more(win)

# Function to determine if a fire occurs based on a given probability
def fire_probability(probability):
    # Generate a random number between 0 and 1, and check if it's less than the given probability
    return random.random() < probability

# Function to check if any neighboring trees are close to a burning tree
def check_trees_close(forest, i, j, probability):
    # Loop through neighboring positions around a tree
    for a in range(-1, 2):  
        for b in range(-1, 2):
            # Check if the neighboring position is within the forest bounds
            if 0 <= i + a < len(forest) and 0 <= j + b < len(forest[0]):
                # Check if the neighboring tree is burning and has a burn level less than 3
                if 0 < forest[i + a][j + b].burn_level < 3:
                    # Check if a fire occurs based on the given probability
                    if fire_probability(probability):
                        return True
    return False

# Function to check and set fire based on probabilities for all non-burning trees
def check_probabilities(win, forest, probability):
    # Create a mask to track which trees need to be updated
    update_mask = [[False for j in range(len(forest[0]))] for i in range(len(forest))]
    # Loop through each tree in the forest
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            # Check if the tree is not burning
            if forest[i][j].burn_level == 0:
                # Check if any neighboring trees are burning and set the update mask accordingly
                update_mask[i][j] = check_trees_close(forest, i, j, probability)
    # Loop through each tree in the forest and set trees on fire based on the update mask
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            if update_mask[i][j]:
                   forest[i][j].burn_more(win)

# Function to convert mouse position to tree position in the forest
def calc_pos(mouse_position, forest):
    x, y = mouse_position.getX(), mouse_position.getY()
    w, h = TREE_WIDTH, TREE_HEIGHT
    # Check if the mouse position is within the valid forest area
    if 0 <= x <= w * len(forest[0]) and 0 <= y <= h * len(forest[0]):
        # Calculate the row and column based on the mouse position
        return int(y / h), int(x / w)
    return None

# Function to simulate the forest fire and display the result
def burn_forest(win, forest, probability):
    step = 0
    # Continue the simulation until there are no more trees on fire
    while forest_on_fire(forest):
        step += 1
        # Update the graphics window to reflect the burning trees
        set_on_fire(forest, win)
        # Check probabilities and set trees on fire accordingly
        check_probabilities(win, forest, probability)
        time.sleep(1)  # Introduce a delay for better visualization
    # Display a message about the fire subsiding
    finish_msg = Button(Point(50, 100), Point(400, 150),
                        f"Fire subsided in {step} steps. Click anywhere to close.")
    finish_msg.draw(win)
    # Wait for a click to close the message and proceed
    while win.checkMouse() is None:
        pass
    finish_msg.undraw()

# Main function to run the forest fire simulation
def main():
    win = GraphWin("Forest Fire Simulation", 750, 350)

    # Create four buttons
    random_start_button = Button(Point(500, 90), Point(700, 120), "Run (Random Start)")
    click_start_button = Button(Point(500, 130), Point(700, 160), "Run (Click to Start)")
    reset_button = Button(Point(500, 170), Point(700, 200), "Reset Simulation")
    quit_button = Button(Point(730, 0), Point(750, 20), "X")

    random_start_button.draw(win)
    click_start_button.draw(win)
    reset_button.draw(win)
    quit_button.draw(win)

    entry_label = Text(Point(600, 35), "Burn Probability:")
    entry_label.draw(win)
    probability_entry = Entry(Point(600, 65), 24)
    probability_entry.draw(win)

    # Create the initial forest grid
    forest = []
    for i in range(10):
        row = []
        for j in range(15):
            row.append(Tree(Point(j*TREE_WIDTH + TREE_WIDTH/2, i*TREE_HEIGHT
                                  + TREE_HEIGHT/2)))
        forest.append(row)
    draw_forest(forest, win)

    # Main event loop
    while True:
        click_point = win.checkMouse()
        if click_point is None:
            continue
        
        # Check which button is clicked and perform the corresponding action
        if random_start_button.point_is_inside(click_point):
            row, cols = random.randint(0, 9), random.randint(0, 14)

            probability = convert_text_to_probability(probability_entry.getText())
            if not probability:
                print("Invalid probability")
            else:
                # Set a random tree on fire and run the simulation
                forest[row][cols].burn_more(win)
                burn_forest(win, forest, probability)

        elif click_start_button.point_is_inside(click_point):
            while True:
                mouse_position = win.getMouse()
                tree_pos = calc_pos(mouse_position, forest)
                if tree_pos:
                    break

            row, cols = tree_pos

            probability = convert_text_to_probability(probability_entry.getText())
            if not probability:
                print("Invalid probability")
            else:
                # Set the clicked tree on fire and run the simulation
                forest[row][cols].burn_more(win)
                burn_forest(win, forest, probability)

        elif reset_button.point_is_inside(click_point):
            # Reset the simulation by creating a new forest grid
            NUM_ROWS = 10
            NUM_COLS = 15
            forest = []
            for i in range(NUM_ROWS):
                row = []
                for j in range(NUM_COLS):
                    tree_position = Point(j * TREE_WIDTH + TREE_WIDTH / 2,
                                          i * TREE_HEIGHT + TREE_HEIGHT / 2)
                    tree = Tree(tree_position)
                    row.append(tree)
                forest.append(row)
            draw_forest(forest, win)

        elif quit_button.point_is_inside(click_point):
            # Close the graphics window when the Quit button is clicked
            break

    win.close()

if __name__ == "__main__":
    main()
