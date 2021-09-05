from itertools import chain
import networkx as nx
from networkx.utils import arbitrary_element
import matplotlib.pyplot as plt
import pylab

def dominating_set(G, start_with=None):
    r"""Finds a dominating set for the graph G.

    A *dominating set* for a graph with node set *V* is a subset *D* of
    *V* such that every node not in *D* is adjacent to at least one
    member of *D* [1]_.

    Parameters
    ----------
    G : NetworkX graph

    start_with : node (default=None)
        Node to use as a starting point for the algorithm.

    Returns
    -------
    D : set
        A dominating set for G.

    Notes
    -----
    This function is an implementation of algorithm 7 in [2]_ which
    finds some dominating set, not necessarily the smallest one.

    See also
    --------
    is_dominating_set

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Dominating_set

    .. [2] Abdol-Hossein Esfahanian. Connectivity Algorithms.
        http://www.cse.msu.edu/~cse835/Papers/Graph_connectivity_revised.pdf

    """
    all_nodes = set(G)
    if start_with is None:
        start_with = arbitrary_element(all_nodes)
    if start_with not in G:
        raise nx.NetworkXError(f"node {start_with} is not in G")
    dominating_set = {start_with}
    dominated_nodes = set(G[start_with])
    remaining_nodes = all_nodes - dominated_nodes - dominating_set
    while remaining_nodes:
        # Choose an arbitrary node and determine its undominated neighbors.
        v = remaining_nodes.pop()
        undominated_neighbors = set(G[v]) - dominating_set
        # Add the node to the dominating set and the neighbors to the
        # dominated set. Finally, remove all of those nodes from the set
        # of remaining nodes.
        dominating_set.add(v)
        dominated_nodes |= undominated_neighbors
        remaining_nodes -= undominated_neighbors
    return dominating_set


def is_dominating_set(G, nbunch):
    """Checks if `nbunch` is a dominating set for `G`.

    A *dominating set* for a graph with node set *V* is a subset *D* of
    *V* such that every node not in *D* is adjacent to at least one
    member of *D* [1]_.

    Parameters
    ----------
    G : NetworkX graph

    nbunch : iterable
        An iterable of nodes in the graph `G`.

    See also
    --------
    dominating_set

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Dominating_set

    """
    testset = {n for n in nbunch if n in G}
    nbrs = set(chain.from_iterable(G[n] for n in testset))
    return len(set(G) - testset - nbrs) == 0


def main():
    w = 20
    h = 20
    d = 100
    # plt.figure(figsize=(w, h), dpi=d)
    G = nx.DiGraph()

    G.add_edge("Ryu", "Ken", weight=1, capacity=3.0)
    G.add_edge("Ryu", "E.Honda", color='r')
    G.add_edge("Ryu", "Chun-Li")
    G.add_edge("Ryu", "Blanka")
    """
    G.add_edge("Ryu", "Guile")
    G.add_edge("Ryu", "T.Hawk")
    G.add_edge("Ryu", "Cammy")
    G.add_edge("Ryu", "Fei-Long")
    G.add_edge("Ryu", "DeeJay")
    G.add_edge("Ryu", "Sagat")
    G.add_edge("Ryu", "Dictator")
    """

    G.add_edge("Ken", "E.Honda", color='r')
    """
    G.add_edge("Ken", "T.Hawk")
    G.add_edge("Ken", "Dictator")
    """

    G.add_edge("E.Honda", "Blanka")
    """
    G.add_edge("E.Honda", "Zangief")
    G.add_edge("E.Honda", "T.Hawk")
    G.add_edge("E.Honda", "Cammy")
    G.add_edge("E.Honda", "Fei-Long")
    G.add_edge("E.Honda", "Dictator")
    """

    G.add_edge("Chun-Li", "Ken")
    G.add_edge("Chun-Li", "E.Honda", color='r')
    G.add_edge("Chun-Li", "Blanka")
    """
    G.add_edge("Chun-Li", "Zangief")
    G.add_edge("Chun-Li", "Guile")
    G.add_edge("Chun-Li", "T.Hawk")
    G.add_edge("Chun-Li", "Cammy")
    G.add_edge("Chun-Li", "DeeJay")
    G.add_edge("Chun-Li", "Boxer")
    G.add_edge("Chun-Li", "Sagat")
    G.add_edge("Chun-Li", "Dictator")
    """

    """
    G.add_edge("Blanka", "Zangief")
    G.add_edge("Blanka", "T.Hawk")
    G.add_edge("Blanka", "Dictator")
    """

    """
    G.add_edge("Zangief", "Ryu")
    G.add_edge("Zangief", "Ken")
    G.add_edge("Zangief", "T.Hawk")
    G.add_edge("Zangief", "DeeJay")
    G.add_edge("Zangief", "Dictator")
    
    G.add_edge("Guile", "Ken")
    G.add_edge("Guile", "E.Honda")
    G.add_edge("Guile", "Blanka")
    G.add_edge("Guile", "Zangief")
    G.add_edge("Guile", "T.Hawk")
    G.add_edge("Guile", "Dictator")
    
    G.add_edge("Dhalsim", "Ryu")
    G.add_edge("Dhalsim", "Ken")
    G.add_edge("Dhalsim", "E.Honda")
    G.add_edge("Dhalsim", "Blanka")
    G.add_edge("Dhalsim", "Zangief")
    G.add_edge("Dhalsim", "Guile")
    G.add_edge("Dhalsim", "T.Hawk")
    G.add_edge("Dhalsim", "Cammy")
    G.add_edge("Dhalsim", "Fei-Long")
    G.add_edge("Dhalsim", "DeeJay")
    G.add_edge("Dhalsim", "Boxer")
    G.add_edge("Dhalsim", "Sagat")
    G.add_edge("Dhalsim", "Dictator")
    #NO EXITE ALQUIEN QUE PIERDA CONTRA T.Hawk
    G.add_edge("Cammy", "Blanka")
    G.add_edge("Cammy", "Zangief")
    G.add_edge("Cammy", "T.Hawk")
    
    G.add_edge("Fei-Long", "Ken")
    G.add_edge("Fei-Long", "Chun-Li")
    G.add_edge("Fei-Long", "Blanka")
    G.add_edge("Fei-Long", "Zangief")
    G.add_edge("Fei-Long", "T.Hawk")
    G.add_edge("Fei-Long", "Cammy")
    
    G.add_edge("DeeJay", "E.Honda")
    G.add_edge("DeeJay", "Blanka")
    G.add_edge("DeeJay", "Zangief")
    G.add_edge("DeeJay", "T.Hawk")
    G.add_edge("DeeJay", "Cammy")
    G.add_edge("DeeJay", "Fei-Long")
    G.add_edge("DeeJay", "Sagat")
    G.add_edge("DeeJay", "Dictator")
    
    G.add_edge("Boxer", "Ryu")
    G.add_edge("Boxer", "Ken")
    G.add_edge("Boxer", "E.Honda")
    G.add_edge("Boxer", "Blanka")
    G.add_edge("Boxer", "Zangief")
    G.add_edge("Boxer", "Guile")
    G.add_edge("Boxer", "T.Hawk")
    G.add_edge("Boxer", "Cammy")
    G.add_edge("Boxer", "Fei-Long")
    G.add_edge("Boxer", "DeeJay")
    G.add_edge("Boxer", "Claw")
    G.add_edge("Boxer", "Sagat")
    G.add_edge("Boxer", "Dictator")
    
    G.add_edge("Claw", "Ryu")
    G.add_edge("Claw", "Ken")
    G.add_edge("Claw", "E.Honda")
    G.add_edge("Claw", "Chun-Li")
    G.add_edge("Claw", "Blanka")
    G.add_edge("Claw", "Zangief")
    G.add_edge("Claw", "Guile")
    G.add_edge("Claw", "Dhalsim")
    G.add_edge("Claw", "T.Hawk")
    G.add_edge("Claw", "Cammy")
    G.add_edge("Claw", "Fei-Long")
    G.add_edge("Claw", "DeeJay")
    G.add_edge("Claw", "Sagat")
    
    G.add_edge("Sagat", "E.Honda")
    G.add_edge("Sagat", "Blanka")
    G.add_edge("Sagat", "Zangief")
    G.add_edge("Sagat", "T.Hawk")
    G.add_edge("Sagat", "Cammy")
    G.add_edge("Sagat", "Fei-Long")
    
    G.add_edge("Dictator", "T.Hawk")
    G.add_edge("Dictator", "Cammy")
    G.add_edge("Dictator", "Fei-Long")
    G.add_edge("Dictator", "Sagat")
    """

    V = dominating_set(G, None)
    print(V)
    print(is_dominating_set(G, V))

    nx.draw(G, arrows=True, arrowsize=20, with_labels=True, node_color='#00b4d9',
            edge_color=('g', 'r', 'g', 'g', 'r', 'g', 'g', 'r'), node_size=2000)
    plt.show()
    return

if __name__ == "__main__":
    main()



