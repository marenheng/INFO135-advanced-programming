# Task 1: Binary Search Worst Case Analysis
"""
When looking for a word in the Italian dictionary: 17 steps
When looking for a word in the French dictionary: 19 steps
The worst case uses log2(N), where N is the number of words in the dictionary.

Italian dictionary (102400 words):
log2(102400) = 16.63 → Rounded up to 17 steps.

French dictionary (480000 words):
log2(480000) = 18.88 → Rounded up to 19 steps.
"""

#task 2 
class LinkedList:
    def __init__(self):
        self.head = None  # The first node (initially empty)

    def print_list(self):
        current = self.head  # Start at the first node
        while current:  # Keep going until we reach the end
            print(current.data)  # Print the data in the node
            current = current.next  # Move to the next node


# Task 3: Reverse a List Using a Stack
class Stack:
    """A simple stack implementation using a Python list."""
    
    def __init__(self):
        self.items = []  # List to store stack elements

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Pop and return the top item from the stack, if not empty."""
        return self.items.pop() if self.items else None

def reverse_list(lst):
    """
    Reverses a list using a stack (LIFO - Last In, First Out).
    Steps:
    1. Push all elements onto the stack.
    2. Pop elements from the stack to get them in reverse order.
    """
    stack = Stack()
    
    # Push all elements onto the stack
    for item in lst:
        stack.push(item)
    
    # Pop elements to get them in reverse order
    reversed_list = []
    while stack.items:
        reversed_list.append(stack.pop())
    
    print("Reversed List:", reversed_list)

# Example usage:
my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)  # Expected output: [5, 4, 3, 2, 1]

"""
Key Takeaways:
- Stacks use the LIFO (Last In, First Out) principle.
- Pushing all items onto a stack stores them in order.
- Popping them out retrieves them in reverse order.
"""