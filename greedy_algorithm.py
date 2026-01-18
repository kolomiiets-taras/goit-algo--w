# Визначення класу Teacher
class Teacher:
    pass

def create_schedule(subjects, teachers):
   pass

if __name__ == '__main__':
    # Множина предметів
    subjects = {}
    # Створення списку викладачів
    teachers = []

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
