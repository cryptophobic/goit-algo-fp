import random
import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    instance_number = 0

    def __init__(self, key, color="skyblue"):
        Node.instance_number += 1
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

def bfs(root, step=1):
    queue = [root]
    shade = 70
    while queue:
        current = queue.pop(0)
        current.color = f"#{shade:02x}{shade:02x}{shade:02x}"
        shade += step
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


def dfs(root, step=1):
    stack = [root]
    shade = 70
    while stack:
        current = stack.pop()
        current.color = f"#{shade:02x}{shade:02x}{shade:02x}"
        shade += step
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

def create_tree(level, bottom_limit=0, top_limit=1000):
    if level == 0:
        return None

    if top_limit - bottom_limit < 2:
        return None

    sub_root = Node(random.randint(bottom_limit + 1, top_limit - 1))
    sub_root.right = create_tree(level - 1, sub_root.val, top_limit)
    sub_root.left = create_tree(level - 1, bottom_limit, sub_root.val)

    return sub_root

root = create_tree(4)

step = 180 // Node.instance_number

# Візуалізація BFS
bfs_order = bfs(root, step)
draw_tree(root)
# Візуалізація DFS
dfs_order = dfs(root, step)
draw_tree(root)
