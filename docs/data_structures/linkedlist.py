from typing import Any, Optional
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    """Node for LinkedList."""
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional['Node'] = None

class LinkedList:
    """LinkedList implementation with visualization."""
    def __init__(self):
        self.head: Optional[Node] = None

    def insertAtBeginning(self, item): 
        # Your implementation is correct, no changes needed
        if self.head:
          new = Node(item)
          new.next = self.head
          self.head = new
        else:
          self.head = Node(item)

    def insertAfter(self, item, index):
        if not self.head:
            print('List is empty')
            return
        
        i = 1
        node = Node(item)
        temp = self.head
        while i < index and temp.next!=None:
          i = i+1
          temp = temp.next
        if i == index:
          node.next= temp.next
          temp.next = node
        else:
          print('This index does not exist in the linked list')

    def insertAtEnd(self, item):
         new_node = Node(item)
         if not self.head:
             self.head = new_node
             return
         
         current = self.head
         while current.next:
             current = current.next
         current.next = new_node

    def deleteItem(self, index):
        if self.head is None:
            print('List is empty')
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        curr_node = self.head
        prev = None
        count = 0
        
        # Traverse until we find the index or reach end
        while curr_node is not None and count < index:
            prev = curr_node
            curr_node = curr_node.next
            count += 1
        
        # Check if index was found
        if curr_node is None:
            print('Index out of range')
            return
        
        # Update the links to skip the deleted node
        if prev is not None:
            prev.next = curr_node.next

    def search(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def traverse(self):
        current = self.head
        if not current:
            print("List is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def visualize(self) -> None:
        """Visualize the linked list."""
        G = nx.DiGraph()
        current = self.head
        prev_node = None
        
        while current:
            G.add_node(id(current), value=current.data)
            if prev_node:
                G.add_edge(id(prev_node), id(current))
            prev_node = current
            current = current.next

        plt.figure(figsize=(12, 3))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                node_size=1500, arrows=True)
        
        labels = {node: f"{G.nodes[node]['value']}" for node in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels)
        
        plt.title("Linked List Visualization")
        plt.show()
    
