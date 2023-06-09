"""
Clone of 2048 game.
"""
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    new_line = [number for number in line if number > 0]

    length_difference_1 = get_difference(line, new_line)

    app_zeros(length_difference_1, new_line)

    if len(new_line) > 1:
        for num in range(len(new_line) - 1):
            if new_line[num] == new_line[num + 1]:
                new_line[num] = new_line[num] * 2
                new_line[num + 1] = 0

    new_line_final = [number for number in new_line if number > 0]

    length_difference_2 = get_difference(new_line, new_line_final)

    app_zeros(length_difference_2, new_line_final)

    return new_line_final


def get_difference(line_a, line_b):
    """
    Takes in 2 lines and returns the difference in length, line_a - line_b
    """
    length_difference = len(line_a) - len(line_b)

    return length_difference


def app_zeros(difference, list_to_app):
    """
    takes in difference of length of lists and appends list with the same amount of zeros
    """
    for num in range(difference):
        list_to_app.append(0)


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.grid = []
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        output_str = ""
        for row in self.grid:
            output_str += ' '.join(map(str, row)) + '\n'

        return output_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """

        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == LEFT:
            grid_to_check_for_change = [row[:] for row in self.grid]

            for idx in range(0, len(self.grid)):
                self.grid[idx] = merge(self.grid[idx])

            if self.grid != grid_to_check_for_change:
                self.new_tile()

        elif direction == RIGHT:
            grid_to_check_for_change = [row[:] for row in self.grid]

            for idx in range(0, len(self.grid)):
                reversed_row = self.grid[idx][::-1]
                merged_reverse_row = merge(reversed_row)
                normal_row = merged_reverse_row[::-1]
                self.grid[idx] = normal_row

            if self.grid != grid_to_check_for_change:
                self.new_tile()

        elif direction == UP:
            grid_to_check_for_change = [row[:] for row in self.grid]

            self.grid = [[row[i] for row in self.grid] for i in range(len(self.grid[0]))]
            for idx in range(0, len(self.grid)):
                self.grid[idx] = merge(self.grid[idx])
            self.grid = [[row[i] for row in self.grid] for i in range(len(self.grid[0]))]

            if self.grid != grid_to_check_for_change:
                self.new_tile()

        else:
            grid_to_check_for_change = [row[:] for row in self.grid]

            self.grid = [[row[i] for row in self.grid] for i in range(len(self.grid[0]))]
            self.grid = [row[::-1] for row in self.grid]

            for idx in range(len(self.grid)):
                self.grid[idx] = merge(self.grid[idx])

            self.grid = [row[::-1] for row in self.grid]
            self.grid = [[row[i] for row in self.grid] for i in range(len(self.grid[0]))]

            if self.grid != grid_to_check_for_change:
                self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        random_num_1 = random.choices([2, 4], weights=[0.9, 0.1])[0]
        zero_indices = []
        for i, row in enumerate(self.grid):
            for j, value in enumerate(row):
                if value == 0:
                    zero_indices.append((i, j))
        random_zero_tile = random.choice(zero_indices)
        self.grid[random_zero_tile[0]][random_zero_tile[1]] = random_num_1

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        value = self.grid[row][col]
        return value


width = int(input('How many columns do you want? '))
height = int(input('How many rows do you want? '))

game = TwentyFortyEight(height, width)
print(game.__str__())
while True:
    direction = input('1 to slide up\n2 to slide down\n3 to slide left\n4 to slide right\n>>')
    if direction not in ['1', '2', '3', '4']:
        print('Not a valid input, try again!')
    else:
        direction = int(direction)
        game.move(direction)
        print(game.__str__())



