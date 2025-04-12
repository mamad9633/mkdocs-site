class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):  # Renamed from is_empty to isEmpty
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        raise IndexError("Queue is empty")
    
    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        raise IndexError("Queue is empty")
    
    def visualize(self):
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 5))
        plt.bar(range(len(self.items)), self.items)
        plt.title('Queue Visualization')
        plt.xlabel('Position')
        plt.ylabel('Value')
        plt.show()
