import numpy as np
from PIL import Image, ImageColor
import cv2
import random
import sys

# Big thanks to BitTickler for the clearest explanation of
# how to adapt Prim's algorithm to maze generation that I have found
# link: https://stackoverflow.com/a/29758926



class Maze:
    """
    A maze data structure, represented as a boolean grid where
    True = Passage
    False = Wall
    """

    def __init__(self, width, height, scale=3, animate=False):
        self._width = width
        self._height = height
        self._scale = scale
        self.grid = np.zeros((width, height), dtype=bool)

        self.__generate(animate)
        self.draw(waitKey=0)

    def __frontier(self, x, y):
        """
        Returns the frontier of cell (x, y)
              The frontier of a cell are all walls with exact distance two,
              diagonals excluded.
        :param x: x coordinate of the cell
        :param y: y coordinate of the cell
        :return: set of all frontier cells
        """
        f = set()
        if x >= 0 and x < self._width and y >= 0 and y < self._height:
            if x > 1 and not self.grid[x-2][y]:
                f.add((x-2, y))
            if x + 2 < self._width and not self.grid[x+2][y]:
                f.add((x+2, y))
            if y > 1 and not self.grid[x][y-2]:
                f.add((x, y-2))
            if y + 2 < self._height and not self.grid[x][y+2]:
                f.add((x, y+2))

        return f

    def __neighbours(self, x, y):
        """
        Returns the neighbours of cell (x, y)
                 The neighbours of a cell are all passages with exact distance two,
                 diagonals excluded.
           :param x: x coordinate of the cell
           :param y: y coordinate of the cell
           :return: set of all neighbours
           """
        n = set()
        if x >= 0 and x < self._width and y >= 0 and y < self._height:
            if x > 1 and self.grid[x-2][y]:
                n.add((x-2, y))
            if x + 2 < self._width and self.grid[x+2][y]:
                n.add((x+2, y))
            if y > 1 and self.grid[x][y-2]:
                n.add((x, y-2))
            if y + 2 < self._height and self.grid[x][y+2]:
                n.add((x, y+2))

        return n

    def __connect(self, x1, y1, x2, y2):
        """
        Connects wall (x1, x2) with passage (x2 , x2), who
        are assumed to be of distance two from each other
            Connecting a wall to a passage implies converting
            that wall and the wall between them to passages
        :param x1: x coordinate of the wall
        :param y1: y coordinate of the wall
        :param x2: x coordinate of the passage
        :param y2: y coordinate of the passage
        """
        x = (x1 + x2) // 2
        y = (y1 + y2) // 2
        self.grid[x1][y1] = True
        self.grid[x][y] = True


    def __generate(self, animate=False):
        """
        Generates a maze using prim's algorithm
        Pseudo code:
        1. All cells are assumed to be walls
        2. Pick cell (x, y) at random and set it to passage
        3. Get frontier fs of (x, y) and add to set s that contains all frontier cells
        4. while s is not empty:
            4a. Pick a random cell (x, y) from s and remove it from s
            4b. Get neighbours ns of (x, y)
            4c. Connect s with random neighbour n from ns
            4d. Add the frontier fs of (x, y) to s

        :param animate: animate the maze
        """
        s = set()
        x, y = (random.randint(0, self._width - 1), random.randint(0, self._height - 1))
        self.grid[x][y] = True
        fs = self.__frontier(x, y)
        for f in fs:
            s.add(f)
        while s:
            x, y = random.choice(tuple(s))
            s.remove((x, y))
            self.draw(highlight=(x,y))
            ns = self.__neighbours(x, y)
            if ns:
                nx, ny = random.choice(tuple(ns))
                self.__connect(x, y, nx, ny)
            fs = self.__frontier(x, y)
            for f in fs:
                s.add(f)

    def get_img(self, pass_colour=(255,255,255), wall_colour=(0,0,0), highlight=None, highlight_colour=(255,0,0)):
        """
        Fetches an image representation of the maze
        :param pass_colour: colour of the passages
        :param wall_colour: colour of the walls
        :param highlight: desired cell to highlight
        :param highligh_colour: colour of highlight
        :return: image of the maze
        """
        im = Image.new('RGB', (self._width, self._height))
        pixels = im.load()
        for x in range(self._width):
            for y in range(self._height):
                if self.grid[x][y]:
                    pixels[x, y] = pass_colour
                else:
                    pixels[x, y] = wall_colour
        if highlight is not None:
            pixels[highlight] = highlight_colour
        return im

    def draw(self, pass_colour=(255, 255, 255), wall_colour=(0, 0, 0), highlight=None, highlight_colour=(255, 0, 0), waitKey=1):
        """
        Draws an image of the maze with cv2.imshow()
        :param pass_colour: colour of the passages
        :param wall_colour: colour of the walls
        :param highlight: desired cell to highlight
        :param highligh_colour: colour of highlight
        :param waitKey: argument to pass to cv2.waitKey()
        """
        img = self.get_img(pass_colour, wall_colour, highlight, highlight_colour).resize((self._width * self._scale, self._height * self._scale)).convert('RGB')
        imcv = np.asanyarray(img)[:,:,::-1].copy()
        cv2.imshow('maze', imcv)
        cv2.waitKey(waitKey);
        # Dirty hack to end execution if window is closed
        if cv2.getWindowProperty('maze', 1) == -1:
            sys.exit()

def main():
    try:
        args = sys.argv
        if len(sys.argv) == 3:
            # arguments specify both maze width and height
            Maze(int(args[1]), int(args[2]), animate=True)
        elif len(sys.argv) == 2:
            # Arguments specify only width
            Maze(int(args[1]), int(args[1]), animate=True)
        elif len(sys.argv) == 2:
            # Default to width = height = 100
            Maze(int(100), int(100), animate=True)
        else:
            # Invalid number of arguments
            raise ValueError

    except ValueError:
        # Can not parse arguments
        print('Please run the program with any of the following: ')
        print('    >python maze.py width:int height:int')
        print('    >python maze.py width:int')
        print('    >python maze.py')
    

if __name__ == "__main__":
    main()






