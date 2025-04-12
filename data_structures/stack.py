from typing import Any, List
import matplotlib.pyplot as plt
import numpy as np

class Stack:
    def __init__(self, para: List = None):
        self.stack: List = para if para is not None else []

    def push(self, newElement: Any) -> None:
        self.stack.append(newElement)

    def pop(self) -> Any:
        if not self.is_empty():
            last_element = self.stack[len(self.stack)-1]
            self.stack.remove(last_element)
            return last_element
        raise IndexError("Stack is empty")

    def is_empty(self) -> bool:
        return len(self.stack) == 0
    
    def peek(self) -> Any:
        if not self.is_empty():
            return self.stack[len(self.stack)-1]
        raise IndexError("Stack is empty")

    def visualize(self) -> None:
        """Visualize the stack vertically."""
        if self.is_empty():
            print("Stack is empty")
            return
            
        plt.figure(figsize=(6, 8))
        y_pos = np.arange(len(self.stack))
        
        plt.barh(y_pos, [1]*len(self.stack), align='center', color='lightblue')
        
        for i, item in enumerate(self.stack):
            plt.text(0.5, i, str(item), ha='center', va='center')
            
        plt.yticks([])
        plt.xticks([])
        plt.title("Stack Visualization")
        plt.xlabel("Top of Stack →")
        plt.gca().invert_yaxis()
        plt.show()
