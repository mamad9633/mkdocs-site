from typing import Any, Optional
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

    def search(self, data):
        current = self.root
        while current:
            if current.data == data:
                return current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_traversal(self):
        if not self.root:
            return
        
        stack = []
        current = self.root
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
                
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
        print()

    def visualize(self) -> None:
        """Visualize the binary search tree."""
        G = nx.Graph()
        
        def add_nodes_edges(node: Node, pos_x: float, pos_y: float, positions: dict) -> None:
            if not node:
                return
                
            G.add_node(id(node), value=node.data)
            positions[id(node)] = (pos_x, pos_y)
            
            if node.left:
                G.add_node(id(node.left), value=node.left.data)
                G.add_edge(id(node), id(node.left))
                add_nodes_edges(node.left, pos_x - 1, pos_y - 1, positions)
                
            if node.right:
                G.add_node(id(node.right), value=node.right.data)
                G.add_edge(id(node), id(node.right))
                add_nodes_edges(node.right, pos_x + 1, pos_y - 1, positions)
        
        positions = {}
        add_nodes_edges(self.root, 0, 0, positions)
        
        plt.figure(figsize=(10, 8))
        nx.draw(G, positions, with_labels=True, node_color='lightgreen', 
                node_size=1500)
        
        labels = {node: f"{G.nodes[node]['value']}" for node in G.nodes()}
        nx.draw_networkx_labels(G, positions, labels)
        
        plt.title("Binary Search Tree")
        plt.axis('equal')
        plt.show()