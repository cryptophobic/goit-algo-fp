import heapq


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
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    start_vertex = 'A'
    shortest_paths = g.dijkstra(start_vertex)

    print("Найкоротші відстані від вершини", start_vertex, ":")
    for vertex, distance in shortest_paths.items():
        print(f"Відстань до {vertex}: {distance}")
