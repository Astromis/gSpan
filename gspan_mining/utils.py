from .graph import Graph


def convert_sentence_graphs( graph_list:list, is_undirected=False, properie="pos"):
    """
    Allows create gSpan graph instance from SentenceGraph
    """
    graphs = []
    for g_idx, graph in enumerate(graph_list):
        tgraph = Graph(g_idx,
                    is_undirected=is_undirected,
                    eid_auto_increment=False)
        for n in graph.nodes():
            tgraph.add_vertex(n, graph.nodes[n][properie])
        for i,e in enumerate(graph.edges()):
            if e[1] == e[0]:
                continue
            tgraph.add_edge(i, e[0], e[1],  '')
        graphs.append(tgraph)
    return graphs
