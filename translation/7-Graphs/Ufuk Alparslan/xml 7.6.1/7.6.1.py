import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt

def parse_graph(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    G = nx.DiGraph()
    positions = {}
    
    # Parse vertices
    for vertex in root.find("Vertices"):
        vertex_id = vertex.get("vertexId")
        x, y = float(vertex.get("x")), float(vertex.get("y"))
        label = vertex.get("label")
        G.add_node(label)
        positions[label] = (x, -y)  # Inverting y for proper visualization
    
    # Parse edges
    for edge in root.find("Edges"):
        tail = edge.get("tail")
        head = edge.get("head")
        G.add_edge(tail, head)
    
    return G, positions

def draw_graph(G, positions):
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos=positions, with_labels=True, node_size=1000, node_color='skyblue', edge_color='black', font_size=12)
    plt.show()

if __name__ == "__main__":
    xml_file = "graph.xml"  # Dosyanın adını uygun şekilde değiştirin
    G, positions = parse_graph(xml_file)
    draw_graph(G, positions)
