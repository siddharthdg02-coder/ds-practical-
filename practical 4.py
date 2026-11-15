class Node:
    def __init__(self, prn, name, role):
        self.prn = prn
        self.name = name
        self.role = role
        self.next = None


A = None
B = None


def add(head, role):
    prn = int(input("Enter student PRN: "))
    name = input("Enter student name: ")
    new = Node(prn, name, role)

    if head is None:
        return new

    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new
    return head


def display(head):
    if head is None:
        print("Club is empty.")
        return

    while head:
        print(head.role, "-> PRN:", head.prn,
              "Name:", head.name)
        head = head.next


def delete(head, prn):
    if head and head.prn == prn:
        return head.next

    temp = head
    while temp and temp.next:
        if temp.next.prn == prn:
            temp.next = temp.next.next
            print("Member deleted.")
            return head
        temp = temp.next

    print("Member not found.")
    return head


def count(head):
    c = 0
    while head:
        c += 1
        head = head.next
    return c


while True:
    print("\n--- PINNACLE CLUB ---")
    print("1. Add President")
    print("2. Add Member")
    print("3. Add Secretary")
    print("4. Delete Member by PRN")
    print("5. Display Members")
    print("6. Count Members")
    print("7. Add Member to Division B")
    print("8. Concatenate Division B into Division A")
    print("9. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        A = add(A, "President")

    elif ch == 2:
        A = add(A, "Member")

    elif ch == 3:
        A = add(A, "Secretary")

    elif ch == 4:
        p = int(input("Enter PRN to delete: "))
        if any_node(A, p):
            A = delete(A, p)
        else:
            B = delete(B, p)

    elif ch == 5:
        print("\nDivision A:")
        display(A)
        print("\nDivision B:")
        display(B)

    elif ch == 6:
        print("Division A members:", count(A))
        print("Division B members:", count(B))

    elif ch == 7:
        B = add(B, "Member")
        print("Record added.")

    elif ch == 8:
        if A is None:
            A = B
        else:
            temp = A
            while temp.next:
                temp = temp.next
            temp.next = B
        B = None
        print("Division B concatenated into Division A.")

    elif ch == 9:
        print("Exiting Pinnacle Club.")
        break

    else:
        print("Invalid choice.")


