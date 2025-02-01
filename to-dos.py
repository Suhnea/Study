def add_task(tasks, category, task):
    if category not in tasks:
        tasks[category] = set()
    tasks[category].add(task)
    print(f"Задача '{task}' добавлена в категорию '{category}'.")

def remove_task(tasks, category, task):
    if category in tasks and task in tasks[category]:
        tasks[category].remove(task)
        print(f"Задача '{task}' удалена из категории '{category}'.")
        if not tasks[category]:  # Если категория пуста, удаляем её
            del tasks[category]
    else:
        print(f"Задача '{task}' в категории '{category}' не найдена.")

def mark_task_done(tasks, done_tasks, category, task):
    if category in tasks and task in tasks[category]:
        done_tasks.add((category, task))
        print(f"Задача '{task}' в категории '{category}' отмечена как выполненная.")
    else:
        print(f"Задача '{task}' в категории '{category}' не найдена.")

def show_tasks(tasks, done_tasks):
    print("\nСписок задач:")
    for category, task_set in tasks.items():
        print(f"\nКатегория: {category}")
        for task in task_set:
            status = "✓" if (category, task) in done_tasks else "✗"
            print(f"  {status} {task}")
    if not tasks:
        print("Задач нет.")

def main():
    tasks = {}  #задачи по категориям
    done_tasks = set()  #выполненные задачи

    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Отметить задачу как выполненную")
        print("4. Показать задачи")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            category = input("Введите категорию: ")
            task = input("Введите задачу: ")
            add_task(tasks, category, task)
        elif choice == "2":
            category = input("Введите категорию: ")
            task = input("Введите задачу: ")
            remove_task(tasks, category, task)
        elif choice == "3":
            category = input("Введите категорию: ")
            task = input("Введите задачу: ")
            mark_task_done(tasks, done_tasks, category, task)
        elif choice == "4":
            show_tasks(tasks, done_tasks)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()