# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    """
    Жадібний алгоритм для складання розкладу.
    На кожному кроці обирає викладача, який може покрити найбільше непокритих предметів.
    При однаковій кількості предметів обирає наймолодшого.
    """
    uncovered_subjects = subjects.copy()
    selected_teachers = []

    while uncovered_subjects:
        best_teacher = None
        max_coverage = 0

        # Знаходимо викладача з найкращим покриттям
        for teacher in teachers:
            # Обчислюємо, скільки непокритих предметів може викладати цей викладач
            coverage = len(teacher.can_teach_subjects & uncovered_subjects)

            if coverage > 0:
                # Якщо цей викладач покриває більше предметів
                if coverage > max_coverage:
                    best_teacher = teacher
                    max_coverage = coverage
                # Якщо покриває однакову кількість, обираємо молодшого
                elif coverage == max_coverage and best_teacher is not None:
                    if teacher.age < best_teacher.age:
                        best_teacher = teacher

        # Якщо не знайшли викладача для покриття предметів, що залишились
        if best_teacher is None:
            return None

        # Призначаємо предмети обраному викладачу
        subjects_to_assign = best_teacher.can_teach_subjects & uncovered_subjects
        best_teacher.assigned_subjects = subjects_to_assign.copy()

        # Оновлюємо множину непокритих предметів
        uncovered_subjects -= subjects_to_assign

        # Додаємо викладача до розкладу
        selected_teachers.append(best_teacher)

    return selected_teachers


if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    # Створення списку викладачів
    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com',
                {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com',
                {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com',
                {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com',
                {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com',
                {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com',
                {'Біологія'})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(
                f"   Викладає предмети: {', '.join(sorted(teacher.assigned_subjects))}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
