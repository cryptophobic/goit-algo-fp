import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def insert(heap_root, key):
    new_node = Node(key)
    if heap_root is None:
        return new_node
    queue = [heap_root]
    while queue:
        current = queue.pop(0)
        if current.left is None:
            current.left = new_node
            return heap_root
        else:
            queue.append(current.left)
        if current.right is None:
            current.right = new_node
            return heap_root
        else:
            queue.append(current.right)

    return heap_root

# Створення бінарної купи
heap_root = Node(10)  # Корінь максимального купи
heap_root = insert(heap_root, 9)
heap_root = insert(heap_root, 8)
heap_root = insert(heap_root, 7)
heap_root = insert(heap_root, 6)
heap_root = insert(heap_root, 5)
heap_root = insert(heap_root, 4)

# Відображення бінарної купи
draw_tree(heap_root)
