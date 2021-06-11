"""
You are given an undirected graph with its maximum degree (the degree of a node
is the number of edges connected to the node).

You need to write a function that can take an undirected graph as its argument
and color the graph legally (a legal graph coloring is when no adjacent nodes
have the same color).

The number of colors necessary to complete a legal coloring is always one more
than the graph's maximum degree.

*Note: We can color a graph in linear time and space. Also, make sure that your
solution can handle a loop in a reasonable way.*
"""
# Definition for a graph node.
# class GraphNode:
#     def __init__(self, label):
#         self.label = label
#         self.neighbors = set()
#         self.color = None

# def color_graph(graph, colors):
#     # Your code here
#     pass

def csFriendCircles(friendships):
    circles = []
    for i in range(len(friendships)):
        for j in range(len(friendships)):
            if friendships[i][j] == 1:
                if not circles:
                    circles.append({i,j})
                for circle in circles:
                    if i in circle:
                        circle.add(j)
                    if j in circle:
                        circle.add(i)
                    else:
                        print('{i},{j}')
                        circles.append({i,j})
    return circles

print(csFriendCircles([[1,1,0], [1,1,1], [0,1,1]]))

