![Example](https://raw.githubusercontent.com/ArneStenkrona/MazeFun/master/MazeFun.PNG)

# MazeFun

This is a simple example of Maze Generation using Prim's algorithm.

## What is Prim's algorithm?

Prim's algorithm is a greedy algorithm for finding a minimum spanning tree for a weighted undirected graph. It can
be modified to generate mazes. The rough idea is to construct a graph with vertices for each "cell/square"
in the maze, with each cell connected to four neighbours; up, down, left and right. By randomizing the weights for
edges between cells, the minimum spanning tree will resemble a maze. A bit confusing, perhaps.



**What it looks like in practice**:

1. Initialize all cells to be walls (black square)

2. Pick cell (x, y) at random and set it to be a passage (white square)

3. Get frontier fs of (x, y) and add to set s that contains all frontier cells

4. while s is not empty:

   - Pick a random cell (x, y) from s and remove it from s
   - Get neighbours ns of (x, y)
   - Connect (x, y) with random neighbour (nx, ny) from ns
   - Add the frontier fs of (x, y) to s            

**Frontier**
The frontier, shown in red, of a cell, shown in green, are all walls within an exact distance of two,
diagonals excluded.

![Example](https://raw.githubusercontent.com/ArneStenkrona/MazeFun/master/Frontier.png)

**Neighbours**
The neighbours, shown in red, of a cell, shown in green, are all passages with exact distance two,
diagonals excluded.

![Example](https://raw.githubusercontent.com/ArneStenkrona/MazeFun/master/Neighbours.png)

**Connecting two cells**
Connecting a wall w, shown in green, to a passage p, shown in orange, assumes that they are
at an exact distance of two of each other, and not on the diagonal.
To connect them we turn the wall w into a passage, as well
as the cell between w and p.

![Example](https://raw.githubusercontent.com/ArneStenkrona/MazeFun/master/Connect.png)

**Further reading**
[Wikipedia:Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm "Prim's algorithm")

[Wikipedia:Minimum spanning tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree "Minimum spanning tree")

## Building and running

* Download the file 'maze.py'
* Make sure you have all the dependencies installed
* run the file in any of the following ways
```
>python maze.py <width> <height>
```
```
>python maze.py <width>
```
```
>python maze.py
```
Where values within '<>' are integers

## Dependencies
numpy (http://www.numpy.org/)

PIL (https://pillow.readthedocs.io/en/stable/)

cv2 (https://pypi.org/project/opencv-python/)

## Authors

* **Arne Stenkrona** 
