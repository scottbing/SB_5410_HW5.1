from SearchFunctions import binarySearchSub
import math


def Dijkstra(graph, source, target):
    # These are all the nodes which have not been visited yet
    unvisited_nodes = graph
    # It will store the shortest distance from one node to another
    shortest_distance = {}
    # This will store the Shortest path between source and target node
    route = []
    # It will store the predecessors of the nodes
    predecessor = {}

    # Iterating through all the unvisited nodes
    for nodes in unvisited_nodes:
        # Setting the shortest_distance of all the nodes as infinty
        shortest_distance[nodes] = math.inf

    # The distance of a point to itself is 0.
    shortest_distance[source] = 0

    # Running the loop while all the nodes have been visited
    while (unvisited_nodes):

        # setting the value of min_node as None
        min_Node = None

        # iterating through all the unvisited node
        for current_node in unvisited_nodes:

            # For the very first time that loop runs this will be called
            if min_Node is None:

                # Setting the value of min_Node as the current node
                min_Node = current_node

            elif shortest_distance[min_Node] > shortest_distance[current_node]:

                # I the value of min_Node is less than that of current_node, set
                # min_Node as current_node

                min_Node = current_node

        # Iterating through the connected nodes of current_node (for
        # # example, a is connected with b and c having values 10 and 3
        # respectively) and the weight of the edges

        for child_node, value in unvisited_nodes[min_Node].items():

            # checking if the value of the current_node + value of the edge
            # that connects this neighbor node with current_node
            # is lesser than the value that distance between current nodes
            # and its connections
            if value + shortest_distance[min_Node] < shortest_distance[child_node]:
                # If true  set the new value as the minimum distance of that connection
                shortest_distance[child_node] = value + shortest_distance[min_Node]

                # Adding the current node as the predecessor of the child node
                predecessor[child_node] = min_Node

        # After the node has been visited (also known as relaxed) remove it from unvisited node
        unvisited_nodes.pop(min_Node)

    # Till now the shortest distance between the source node and target node
    # has been found. Set the current node as the target node
    node = target

    # Starting from the goal node, we will go back to the source node and
    # see what path we followed to get the smallest distance
    while node != source:

        # As it is not necessary that the target node can be reached from # the source node, we must enclose it in a try block
        try:
            route.insert(0, node)
            node = predecessor[node]
        except Exception:
            print('Path not reachable')
            break
    # Including the ssource in the path
    route.insert(0, source)

    # If the node has been visited,
    if shortest_distance[target] != math.inf:
        # print the shortest distance and the path taken
        print('Shortest distance is ' + str(shortest_distance[target]))
        print('And the path is ' + str(route))
    # Remove the below comment if you want to show the the shortest distance
    # from source to every other node
    # print(shortest_distance)

    return (predecessor, shortest_distance)

# end def Dijkstra(graph, source, target):

def prompt():
    entry = input("Enter your desired $ amount to spend (Q to quit):")
    if entry.isnumeric():   #for out purpsoses, and non number is q
        return entry
    else:
        return 'Q'

#end def prompt():

def main():
    graph = {'s': {'r': 5, 'p': 0},
            'r': {'b': 15, 'd': 20},
            'p': {'b': 30, 'd': 35},
            'b': {'g': 20},
            'd': {'g': 10},
            'g': {}
            }
    # Calling the function ith source an target
    pred, table = Dijkstra(graph, 's', 'g')
    table = sorted(table.items(), key=lambda x: x[1])
    print(table)
    entry = prompt()
    while entry != 'Q':
        amounts = [amount(1) for amount in table]
        subi = binarySearchSub(amounts, 0, len(amounts)-1, int(entry))
        print(subi)
        print("you should buy {0} for ${1}".format(table[subi][0],
                                                   table[subi][1]))

        entry = prompt()
    # print("All values are: ", table)
    # for key in pred.keys():
    #     print("The shortest path to {0} is through {1}.".format(key, pred[key]))
#end def main():

if __name__ == '__main__':
    main()

# graph = {'a': {'b': 5, 'c': 2}, 'b': {'c': 1, 'd': 3}, 'c': {'b': 3, 'd': 7}, 'd': {'e': 7}, 'e': {'d': 9}}
# # Calling the function with source as 'a' and target as 'e'.
# Dijkstra(graph, 'a', 'e')