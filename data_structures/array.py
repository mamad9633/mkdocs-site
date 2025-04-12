from typing import Any, Optional
import matplotlib.pyplot as plt
import numpy as np

class Array:
    """Array implementation with visualization capabilities."""
    
    def __init__(self) -> None:
        self.array: list = []

    def insert(self, item: Any) -> None:
        self.array.append(item)

    def delete(self, index: int) -> Any:
        if 0 <= index < len(self.array):
            return self.array.pop(index)
        raise IndexError("Index out of range")

    def search(self, item: Any) -> int:
        for i in range(len(self.array)):
            if self.array[i] == item:
                return i
        return -1

    def get(self, index: int) -> Any:
        if 0 <= index < len(self.array):
            return self.array[index]
        raise IndexError("Index out of range")

    def length(self) -> int:
        return len(self.array)

    def display(self) -> None:
        print(self.array)

    def visualize(self) -> None:
        """Visualize array elements."""
        plt.figure(figsize=(10, 2))
        plt.bar(range(len(self.array)), self.array)
        plt.title("Array Visualization")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.show()