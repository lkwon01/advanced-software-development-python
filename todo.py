#Name: Laura Collins
#V-number:V00763363
#Date: 2026-03-07
#To Do List Application
#Develop a simple to-do list application that allows users to add tasks, remove tasks by index, and print the current list of tasks.


def add_task(task, to_do):
    to_do.append(task)
    print(f'Task "{task}" added to the to-do list.')

    
def remove_task(index, to_do):
    try:
        removed_task = to_do.pop(index)
        print(f'Task "{removed_task}" removed from the to-do list.')
    except IndexError:
        print(f"Error: No task at index {index}. Please enter a valid index.")


def print_to_do(to_do):
    print("To Do List:")
    for i in range(len(to_do)):
        print(f'[{i}]: {to_do[i]}')
        
def main():
    to_do = []
    add_task("Buy groceries", to_do)
    add_task("Do laundry", to_do)
    add_task("Clean bathroom", to_do)
    add_task("Wash dishes", to_do)
    print_to_do(to_do)
    remove_task(2, to_do)
    print_to_do(to_do)
    remove_task(0, to_do)
    print_to_do(to_do)
    print('i am testing my module')

if __name__ == '__main__':    
    main()