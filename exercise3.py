import heapq

edges = [
    ("Вулиця", "Коридор", 5),
    ("Коридор", "Комора", 1),
    ("Коридор", "Туалет", 2),
    ("Коридор", "Ванна", 3),
    ("Коридор", "Кухня", 4),
    ("Коридор", "Кабінет", 2),
    ("Коридор", "Вітальня", 4),
    ("Вітальня", "Спальня", 1),
    ("Спальня", "Балкон", 1),
    ("Балкон", "Вулиця", 20),
    ("Вітальня", "Вулиця", 20),
    ("Кабінет", "Вулиця", 20),
    ("Кухня", "Вулиця", 20),
]


class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:  # У випадку, якщо v ще не додано
            self.edges[v] = []
        self.edges[u].append((v, weight))

    def dijkstra(self, start):
        # Відстані до всіх вершин
        distances = {vertex: float('inf') for vertex in self.edges}
        distances[start] = 0

        # Пріоритетна черга (бінарна купа)
        priority_queue = [(0, start)]  # (відстань, вершина)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Перевірка на вже знайдену відстань
            if current_distance > distances[current_vertex]:
                continue

            # Переглядаємо сусідів
            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight

                # Якщо знайдено коротший шлях
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


if __name__ == "__main__":
    g = Graph()
    for start, finish, weight in edges:
        g.add_edge(start, finish, weight)

    start_vertex = 'Вулиця'
    shortest_paths = g.dijkstra(start_vertex)

    print("Найкоротші відстані від вершини", start_vertex, ":")
    for vertex, distance in shortest_paths.items():
        print(f"Відстань до {vertex}: {distance}")
