# Enter your code here. Read input from STDIN. Print output to STDOUT

# Given a 2D grid that represents a map of the sky, count the number of clouds. A cloud is represented as a group of 1's connected horizontally or vertically.

#sky = [
#    [0, 1, 1, 0],
#    [1, 1, 0, 1],
#    [0, 0, 1, 0],
#    [1, 1, 1, 0]
#]

def countClouds(2d_input):
    # iterate over all elements
    # if element is 1
        # recurse over x + 1 and y + 1 until 0 is found
