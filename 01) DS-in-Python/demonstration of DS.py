import ast
import heapq

from collections import deque

class node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class treenode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
            last.next = new_node

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(f"[{current.data}]")
            current = current.next
        return " -> ".join(elements) + "-> None"

raw = input("Entre the data you want to be demonstrated: ")

print("\n Available data structures: List, Tuple, Set, Linked list, Stack, Queue, Graph, Heap, Recursion, Tree")
structure = input("\n Select a data structure to be demonstrated from the ones listed above: ")

parsed = []

for item in raw:
    try:
        parsed.append(int(item))
    except ValueError:  
        try:
            parsed.append(float(item))
        except ValueError:

                 parsed.append(item)

print("\n Demonstration")


#if user chooses List (illustration)

if structure == "List":
    result = list(parsed)
    print(f"Demonstration of List: {result}")


#if user chooses Tuple (illustration)

elif structure == "Tuple":
    result = tuple(parsed)
    print(f"Demonstration of Tuple: {result}")


#if user chooses Set (illustration)

elif structure == "Set":
    result = set(parsed)
    print(f"Demonstration of Set: {result}")


#if user chooses Linked List (illustration)

elif structure == "Linked List":
    ll = linkedlist()
    for ll in parsed:
        ll.append(parsed)
    print(f"Demonstation of LinkedList: {ll.display()}")


#if user chooses Stack (illustration)

elif structure == "Stack":  
    stack = []
    for element in parsed:
        stack.append(element)
    print(f"Demonstration of Stack after pushing: {stack}")

    if stack: 
        removed_item = stack.pop()
        print(f"LIFO: {removed_item}")
        print(f"Stack after popping: {stack}")
    else:
        print("Stack is empty")


#if user chooses Queue (illustration)

elif structure == "Queue":
    queue = deque()
    for elements in parsed:
        queue.append(elements)
        print(f"Demonstration of Queue after enqueing: list{queue}")
        
        if queue:
            removed_item = queue.popleft()
            print(f"Dequeued item: {removed_item}")
            print(f"Demonstration of Queue after dequeuing: list{queue}")
        else: 
            print("Queue is empty")


#if user chooses Graph (illustration)

elif structure == "Graph":
    graph = {}
    for elements in parsed:
        graph[elements] = []
    for i in range(len(parsed) - 1):
        current_node = parsed[i]
    next_node = parsed[i + 1]
    graph[current_node].append(next_node)
    print(f"Demonstation of graph (adjecent):")
    for node, edges in graph.items():
        print(f"Node [{node}] connects to -> Neighbours {edges}")


#if user chooses Heap (illustration)

elif structure == "Heap":
    heap = []
    for element in parsed:
        try:
            heapq.heappush(heap, float(element))
        except ValueError:
            heapq.heappush(heap, element)
        if heap:
            smallest = heapq.heappop(heap)
            print(f"Popped smallest item: {smallest}")
            print(f"Heap after popping: {heap}")


#if user chooses Recursion (illustration)

elif structure == "Recursion":
    print("Demonstration of recursion (sum of numbers):")
numeric_items = []
if isinstance(item, (int, float)):
        numeric_items.append(item)

        def recursive_sum(lst):
            if not lst:
                return 0
            return lst[0] + recursive_sum(lst[1:])

        if numeric_items:
            total_sum = recursive_sum(numeric_items)
            print(f"List of numbers: {numeric_items}")
        else:
            print(f"No numeric data found in parsed list to perform recursive math")


#if user chooses Tree (illustration)

elif structure == "Tree":
    print(f"Demonstration of Tree (BST):")

    def insert_bst(root, data):
        if root is None:
            return treenode(data)
        if str(data) < str(root.data):
            root.left = insert_bst(root.left, data)
        else:
            root.right = insert_bst(root.right, data)
        return root

    def inorder_traverse(root, result_list):
        if root:
            inorder_traverse(root.left, result_list)
            result_list.append(root.data)
            inorder_traverse(root.right, result_list)

if parsed:
    root_node = None
for element in parsed:
    root_node = insert_bst(root_node, element)
    
    sorted_elements = []
    inorder_traverse(root_node, sorted_elements)
    print(f"In order traversal of the built tree (sorted): {sorted_elements}")
else:
    print("No data available to construct a tree")