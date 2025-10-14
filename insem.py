# 🗺️ Map Coloring Application using NetworkX
import networkx as nx
import matplotlib.pyplot as plt

def color_map(graph):
    """
    Color the graph such that no two adjacent nodes have the same color.
    Returns a dictionary {node: color}.
    """
    colors = nx.coloring.greedy_color(graph, strategy='largest_first')
    return colors

def visualize_colored_map(graph, colors):
    """
    Display the colored map using matplotlib.
    """
    plt.figure(figsize=(6, 5))

    # Define a color palette
    color_palette = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink']
    node_colors = [color_palette[colors[node] % len(color_palette)] for node in graph.nodes()]

    nx.draw(
        graph,
        with_labels=True,
        node_color=node_colors,
        node_size=1000,
        font_color='white',
        font_weight='bold'
    )

    plt.title("Map Coloring Visualization")
    plt.show()

def main():
    # Create a graph representing countries (or map regions)
    G = nx.Graph()

    # Example map (simple 6-region adjacency)
    edges = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'C'), ('B', 'D'),
        ('C', 'E'), ('D', 'E'),
        ('D', 'F'), ('E', 'F')
    ]

    G.add_edges_from(edges)

    # Color the map
    color_assignment = color_map(G)
    print("Color assignment:", color_assignment)

    # Visualize
    visualize_colored_map(G, color_assignment)

if __name__ == "__main__":
    main()
