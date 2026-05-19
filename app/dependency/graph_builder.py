import networkx as nx

from app.dependency.dependency_mapper import generate_dependencies


def build_graph():

    dependencies = generate_dependencies()

    graph = nx.DiGraph()

    for dependency in dependencies:

        source = dependency["source"]
        target = dependency["target"]
        score = dependency["influence_score"]

        graph.add_edge(
            source,
            target,
            weight=score
        )

    return graph


if __name__ == "__main__":

    graph = build_graph()

    print("\nDEPENDENCY GRAPH:\n")

    for edge in graph.edges(data=True):
        print(edge)