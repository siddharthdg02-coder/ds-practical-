seats = [['F' for j in range(7)] for i in range(10)]

# Initially booked seats
seats[2][0] = 'X'
seats[2][4] = 'X'
seats[3][3] = 'X'
seats[3][5] = 'X'
seats[4][5] = 'X'
seats[5][0] = 'X'
seats[5][3] = 'X'
seats[6][3] = 'X'
seats[6][6] = 'X'
seats[7][6] = 'X'
seats[8][3] = 'X'
seats[9][0] = 'X'

while True:

    print("\n--- CINEMAX TICKET BOOKING ---")
    print("1. Display Available Seats")
    print("2. Book a Seat")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        print("\nAVAILABLE SEATS (F = Free, X = Booked)")
        print("       1 2 3 4 5 6 7")

        for i in range(10):
            print("Row", i + 1, ":", end=" ")

            for j in range(7):
                print(seats[i][j], end=" ")

            print()

    elif choice == 2:

        row = int(input("Enter row number (1-10): "))
        seat = int(input("Enter seat number (1-7): "))

        if row < 1 or row > 10 or seat < 1 or seat > 7:
            print("Invalid row or seat number!")

        elif seats[row-1][seat-1] == 'X':
            print("Seat already booked!")

        else:
            seats[row-1][seat-1] = 'X'
            print("Seat booked: Row", row, ", Seat", seat)

    elif choice == 3:

        row = int(input("Enter row number (1-10): "))
        seat = int(input("Enter seat number (1-7): "))

        if row < 1 or row > 10 or seat < 1 or seat > 7:
            print("Invalid row or seat number!")

        elif seats[row-1][seat-1] == 'F':
            print("Seat is not booked!")

        else:
            seats[row-1][seat-1] = 'F'
            print("Booking cancelled: Row", row, ", Seat", seat)

    elif choice == 4:
        print("Thank you for using Cinemax!")
        break

    else:
        print("Invalid choice! Please try again.")
