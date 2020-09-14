from Graph import Graph


def main():

    #make graph
    g = Graph()
    #count the nodes in hte image. 6
    g.add_vertex('s')
    g.add_vertex('b')
    g.add_vertex('p')
    g.add_vertex('d')
    g.add_vertex('r')
    g.add_vertex('b')
    #count the edges in the image. 8
    g.add_edge('s', 'r', 6)
    g.add_edge('s', 'p', 0)
    g.add_edge('r', 'b', 15)
    g.add_edge('r', 'd', 20)
    g.add_edge('p', 'b', 35)
    g.add_edge('p', 'd', 35)
    g.add_edge('d', 'g', 10)
    g.add_edge('b', 'g', 20)

    #delete test after run
    for v in g:
        print('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))


if __name__ == '__main__':
    main()