import numpy as np
import matplotlib.pyplot as plt

# Задана таблиця значень функції корисності
utility = np.array([0.14, 0.55, 0.66, 0.73, 0.78, 0.83, 0.87, 0.93, 0.98])
money = np.array([-3000, -1000, 0, 1000, 2000, 3000, 4000, 6000, 8000])

# Визначення типу функції корисності (розрахунок похідної)
derivative = np.diff(utility) / np.diff(money)

if np.all(derivative > 0):
    print("Функція корисності налаштована на ризик.")
else:
    print("Функція корисності не налаштована на ризик або є лінійною.")

# Вирішення про доцільність гри в орлянку
start_capital = 3000
bet_heads = -1000
bet_tails = 1500

# Оцінка результатів гри
result_heads = start_capital + bet_heads
result_tails = start_capital + bet_tails

# Знаходження відповідних значень корисності для результатів гри
index_heads = np.argmin(np.abs(money - result_heads))
index_tails = np.argmin(np.abs(money - result_tails))

utility_heads = utility[index_heads]
utility_tails = utility[index_tails]

print(f"Корисність при ставці на орла (-1000): {utility_heads}")
print(f"Корисність при ставці на решку (+1500): {utility_tails}")

# Побудова графіку функції корисності
plt.figure(figsize=(8, 6))
plt.plot(money, utility, marker='o', linestyle='-', color='b')
plt.xlabel('Гроші')
plt.ylabel('Корисність')
plt.title('Функція корисності')
plt.grid(True)

# Виведення графіка
plt.show()
