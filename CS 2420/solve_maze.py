#This method reads the maze from a file, and gets the starting location
#Completed by Dr B
def read_maze_from_file(filename):
    file = open(filename, "r")
    line = file.readline()
    (x,y) = line.split(" ")
    maze = []
    for line in file:
        maze.append(line.replace("\n","").replace("\r","").split(" "))
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                x = i
                y = j
    return x, y, maze

#this method prints the maze in a nice format
#Completed by Dr B
def pretty_print(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j], end="")
        print()

# This is not just a single base case and a single recursive case.
# If the maze is solved by going left - there is a solution
# If the maze is solved by going right - there is a solution
# If the maze is solved by going up - there is  a solution
# If the maze is solved by going down - there is  a solution
#
# Depending on how you go up, down, left, and right
# there might be several base cases, like, on a wall,
# on the start, on the end, on a trail already marked...
#
# This function is for you to complete
def maze_traversal(current_x, current_y, maze):
	# Note, you should not need any loops.  Your first instinct might be to add them, but ignore that instinct
	# Loops are for iteration, not recursion

    #base case(s) - first one done for you
    if(maze[current_x][current_y] == "#"):
        return False
    if(maze[current_x][current_y] == "x"): # visited already
        return False
    if(maze[current_x][current_y] == "E"):
        return True

    maze[current_x][current_y] = "x"

    if maze_traversal(current_x + 1, current_y, maze) == True:
        return True
    if maze_traversal(current_x - 1, current_y, maze) == True:
        return True
    if maze_traversal(current_x, current_y + 1, maze) == True:
        return True
    if maze_traversal(current_x, current_y - 1, maze) == True:
        return True

# This method is sometimes called a "driver" method
# because it sets up the variables for the recursive case
# Completed by Dr B
def solve_maze(filename):
    # setup all the variables correctly
    print("Working on maze " + filename)
    (start_x, start_y, maze) = read_maze_from_file(filename)
    pretty_print(maze)
    print("The starting location is: " + str(start_x) + " " + str(start_y))
    #replace the S with a . so the recursion is easier
    maze[start_x][start_y] = "."
    maze_traversal(start_x,start_y,maze)

    #Add back in the S so we know where we started from
    maze[start_x][start_y] = "S"
    pretty_print(maze)
    

# Uncomment these as necessary
#solve_maze("CS 2420/Maze1_easy.txt")
solve_maze("CS 2420/Maze2_manyChoices.txt")
#solve_maze("CS 2420/Maze3_Large.txt")
#solve_maze("CS 2420/Maze4_No_Solution.txt")
#solve_maze("CS 2420/Maze5_Larger.txt")


