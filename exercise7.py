import numpy as np
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    # Ініціалізація лічильника для сум
    sum_counts = {i: 0 for i in range(2, 13)}  # Суми від 2 до 12

    # Симуляція кидків кубиків
    for _ in range(num_rolls):
        die1 = np.random.randint(1, 7)  # Кидок першого кубика
        die2 = np.random.randint(1, 7)  # Кидок другого кубика
        total = die1 + die2
        sum_counts[total] += 1  # Збільшення лічильника для отриманої суми

    # Обчислення ймовірностей
    probabilities = {total: count / num_rolls for total, count in sum_counts.items()}
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color='skyblue')
    plt.xticks(sums)
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум двох кубиків')
    plt.ylim(0, max(probs) + 0.05)  # Встановлення меж для осі y
    plt.grid(axis='y')
    plt.show()

if __name__ == "__main__":
    # Кількість кидків кубиків
    num_rolls = 1000000

    # Проведення симуляції
    probabilities = simulate_dice_rolls(num_rolls)

    # Виведення ймовірностей
    print("Ймовірності сум:")
    for total, prob in probabilities.items():
        print(f"Сума {total}: {prob:.4f}")

    # Побудова графіка ймовірностей
    plot_probabilities(probabilities)
