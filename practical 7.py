queue = []
front = 0

M = int(input("Enter maximum number of orders: "))

while True:
    print("\n--- PIZZA PARLOUR ---")
    print("1. Accept Order")
    print("2. Serve Order")
    print("3. Display Orders")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(queue) - front < M:
            order = input("Enter pizza order: ")
            queue.append(order)
            print("Order accepted:", order)
        else:
            print("Queue is Full! Cannot accept more orders.")

    elif choice == 2:
        if front == len(queue):
            print("Queue is Empty! No orders to serve.")
        else:
            print("Order served:", queue[front])
            front += 1

    elif choice == 3:
        if front == len(queue):
            print("No pending orders.")
        else:
            print("\nPending Orders:")
            for i in range(front, len(queue)):
                print(queue[i])

    elif choice == 4:
        print("Thank you for visiting Pizza Parlour!")
        break

    else:
        print("Invalid choice! Please try again.")
