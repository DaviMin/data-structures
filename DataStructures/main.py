from fronta import CharQueue
from zasobnik import IntegerStack


def main_queue():
    queue_size = int(input("Enter the size of the queue: "))
    char_queue = CharQueue(queue_size)

    while True:
        print("\nMenu:")
        print("1. Check if the queue is empty")
        print("2. Check if the queue is full")
        print("3. Add an element to the queue (Enqueue)")
        print("4. Delete an element from the queue (Dequeue)")
        print("5. Display all queue elements")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Queue is empty." if char_queue.is_empty() else "Queue is not empty.")

        elif choice == '2':
            print("Queue is full." if char_queue.is_full() else "Queue is not full.")

        elif choice == '3':
            if char_queue.is_full():
                print("Queue is full. Cannot add new element.")
            else:
                element = input("Enter the character to enqueue: ")
                char_queue.enqueue(element)
                print("Element enqueued.")

        elif choice == '4':
            item = char_queue.dequeue()
            if item is not None:
                print(f"Dequeued element: {item}")
            else:
                print("Queue is empty. Cannot dequeue.")

        elif choice == '5':
            char_queue.show()

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")


def main_stack():
    stack_size = int(input("Enter the size of the stack: "))
    stack = IntegerStack(stack_size)

    while True:
        print("\nMenu:")
        print("1. Push an integer onto the stack")
        print("2. Pop an integer from the stack")
        print("3. Count integers in the stack")
        print("4. Check if the stack is empty")
        print("5. Check if the stack is full")
        print("6. Clear the stack")
        print("7. Peek at the top integer")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = int(input("Enter an integer to push: "))
            if stack.push(item):
                print("Integer pushed onto the stack.")
            else:
                print("Stack is full. Cannot push.")

        elif choice == '2':
            item = stack.pop()
            if item is not None:
                print(f"Popped integer: {item}")
            else:
                print("Stack is empty. Cannot pop.")

        elif choice == '3':
            print(f"Number of integers in stack: {stack.count()}")

        elif choice == '4':
            print("Stack is empty." if stack.is_empty() else "Stack is not empty.")

        elif choice == '5':
            print("Stack is full." if stack.is_full() else "Stack is not full.")

        elif choice == '6':
            stack.clear()
            print("Stack cleared.")

        elif choice == '7':
            item = stack.peek()
            if item is not None:
                print(f"Top integer: {item}")
            else:
                print("Stack is empty.")

        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_stack()