items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    # Розрахунок співвідношення калорій до вартості для кожної страви
    items_sorted = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    total_cost = 0
    selected_items = []

    for item, properties in items_sorted:
        if total_cost + properties['cost'] <= budget:
            selected_items.append(item)
            total_calories += properties['calories']
            total_cost += properties['cost']

    return selected_items, total_calories, total_cost


def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    total_cost = 0

    # Створення таблиці для зберігання максимальних калорій для кожного бюджету
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнення таблиці
    for i in range(1, n + 1):
        item_name, properties = item_list[i - 1]
        for j in range(budget + 1):
            if properties['cost'] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - properties['cost']] + properties['calories'])
            else:
                dp[i][j] = dp[i - 1][j]

    # Визначення вибраних страв
    total_calories = dp[n][budget]
    selected_items = []
    j = budget

    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name, properties = item_list[i - 1]
            selected_items.append(item_name)
            total_cost += properties['cost']
            j -= properties['cost']

    selected_items.reverse()  # Відновлення порядку вибраних страв
    return selected_items, total_calories, total_cost


# Тестування обох алгоритмів
budget = 100

greedy_items, greedy_calories, greedy_cost = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_items)
print("Загальна калорійність:", greedy_calories)
print("Загальна вартість:", greedy_cost)

dp_items, dp_calories, dp_cost = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Вибрані страви:", dp_items)
print("Загальна калорійність:", dp_calories)
print("Загальна вартість:", dp_cost)

