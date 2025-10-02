import sys
from schedule_manager import ScheduleManager
from task_factory import TaskFactory
from observer import ConsoleObserver

def menu():
    print("\nAstronaut Daily Schedule Organizer")
    print("1) Add task")
    print("2) Remove task")
    print("3) View tasks")
    print("4) Mark task complete")
    print("5) Clear all tasks")
    print("6) Exit")

def main():
    manager = ScheduleManager.get_instance()
    manager.register_observer(ConsoleObserver())

    while True:
        menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Task name: ")
            start = input("Start (HH:MM): ")
            end = input("End (HH:MM): ")
            pr = input("Priority (High/Medium/Low): ") or "Medium"
            try:
                task = TaskFactory.create(name, start, end, pr)
                manager.add_task(task)
                print("Task added.")
            except Exception as e:
                print("Error:", e)
        elif choice == "2":
            name = input("Task to remove: ")
            try:
                manager.remove_task(name)
                print("Removed.")
            except Exception as e:
                print("Error:", e)
        elif choice == "3":
            tasks = manager.view_tasks()
            if not tasks:
                print("No tasks scheduled.")
            else:
                for t in tasks:
                    print(t)
        elif choice == "4":
            name = input("Task to complete: ")
            try:
                manager.mark_complete(name)
                print("Marked complete.")
            except Exception as e:
                print("Error:", e)
        elif choice == "5":
            confirm = input("Clear all? (y/N): ")
            if confirm.lower() == "y":
                manager.clear_all()
                print("Cleared all tasks.")
        elif choice == "6":
            print("Bye."); sys.exit(0)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
