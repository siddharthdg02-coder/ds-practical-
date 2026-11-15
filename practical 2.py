n = int(input("Enter number of students (minimum 5): "))

# Accept percentages
marks = []

for i in range(n):
    percentage = float(input("Enter percentage of student " + str(i + 1) + ": "))
    marks.append(percentage)


# Selection Sort
selection = marks.copy()

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if selection[j] < selection[min_index]:
            min_index = j

    selection[i], selection[min_index] = selection[min_index], selection[i]


# Bubble Sort
bubble = marks.copy()

for i in range(n):
    for j in range(0, n - i - 1):
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]


# Display sorted results
print("\nSelection Sort (Ascending):", selection)
print("Bubble Sort (Ascending):", bubble)


# Display Top Five Scores
print("\nTop Five Scores:")

for i in range(n - 1, max(n - 6, -1), -1):
    print(bubble[i])
