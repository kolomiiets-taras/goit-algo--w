import random
import math


# Визначення функції Сфери
def sphere_function(x):
    return sum(xi ** 2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    """
    Алгоритм підйому на гору (Hill Climbing).
    На кожній ітерації генерує сусідів і вибирає кращого.
    """
    # Генерація початкової точки
    n_dims = len(bounds)
    current = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(n_dims)]
    current_value = func(current)

    step_size = 0.1  # Розмір кроку для генерації сусідів

    for iteration in range(iterations):
        # Генерація сусідів у всіх напрямках
        neighbors = []
        for i in range(n_dims):
            # Сусід зі збільшенням по i-й координаті
            neighbor_plus = current.copy()
            neighbor_plus[i] = min(bounds[i][1], current[i] + step_size)
            neighbors.append(neighbor_plus)

            # Сусід зі зменшенням по i-й координаті
            neighbor_minus = current.copy()
            neighbor_minus[i] = max(bounds[i][0], current[i] - step_size)
            neighbors.append(neighbor_minus)

        # Знаходимо найкращого сусіда
        best_neighbor = None
        best_neighbor_value = current_value

        for neighbor in neighbors:
            neighbor_value = func(neighbor)
            if neighbor_value < best_neighbor_value:
                best_neighbor = neighbor
                best_neighbor_value = neighbor_value

        # Перевірка умови зупинки
        if best_neighbor is None or abs(current_value - best_neighbor_value) < epsilon:
            break

        # Переміщення до кращого сусіда
        current = best_neighbor
        current_value = best_neighbor_value

        # Адаптивне зменшення розміру кроку
        step_size *= 0.99

    return current, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    """
    Випадковий локальний пошук.
    На кожній ітерації генерує випадкового сусіда і приймає його, якщо він кращий.
    """
    # Генерація початкової точки
    n_dims = len(bounds)
    current = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(n_dims)]
    current_value = func(current)

    step_size = 0.5  # Початковий розмір кроку

    for iteration in range(iterations):
        # Генерація випадкового сусіда
        neighbor = []
        for i in range(n_dims):
            # Додаємо випадкове відхилення до поточної координати
            delta = random.uniform(-step_size, step_size)
            new_coord = current[i] + delta
            # Обмежуємо координату межами
            new_coord = max(bounds[i][0], min(bounds[i][1], new_coord))
            neighbor.append(new_coord)

        neighbor_value = func(neighbor)

        # Приймаємо сусіда, якщо він кращий
        if neighbor_value < current_value:
            # Перевірка умови зупинки
            if abs(current_value - neighbor_value) < epsilon:
                current = neighbor
                current_value = neighbor_value
                break

            current = neighbor
            current_value = neighbor_value

        # Адаптивне зменшення розміру кроку
        step_size *= 0.995

    return current, current_value


# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95,
                        epsilon=1e-6):
    """
    Імітація відпалу (Simulated Annealing).
    Приймає гірші розв'язки з ймовірністю, що залежить від температури.
    """
    # Генерація початкової точки
    n_dims = len(bounds)
    current = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(n_dims)]
    current_value = func(current)

    best = current.copy()
    best_value = current_value

    current_temp = temp

    for iteration in range(iterations):
        # Перевірка умови зупинки за температурою
        if current_temp < epsilon:
            break

        # Генерація сусіда
        neighbor = []
        for i in range(n_dims):
            # Розмір кроку залежить від температури
            delta = random.uniform(-1, 1) * (current_temp / temp)
            new_coord = current[i] + delta
            # Обмежуємо координату межами
            new_coord = max(bounds[i][0], min(bounds[i][1], new_coord))
            neighbor.append(new_coord)

        neighbor_value = func(neighbor)

        # Обчислення різниці енергій
        delta_e = neighbor_value - current_value

        # Приймання рішення про перехід
        if delta_e < 0:
            # Кращий розв'язок - завжди приймаємо
            current = neighbor
            current_value = neighbor_value

            # Оновлюємо найкращий розв'язок
            if current_value < best_value:
                if abs(best_value - current_value) < epsilon:
                    best = current.copy()
                    best_value = current_value
                    break
                best = current.copy()
                best_value = current_value
        else:
            # Гірший розв'язок - приймаємо з певною ймовірністю
            probability = math.exp(-delta_e / current_temp)
            if random.random() < probability:
                current = neighbor
                current_value = neighbor_value

        # Охолодження
        current_temp *= cooling_rate

    return best, best_value


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
