def linear_search(roll_numbers, key):
    for i in range(len(roll_numbers)):
        if roll_numbers[i] == key:
            return i
        return -1

n = int(input("Enter number of students: "))

roll_numbers = []

print("Enter roll numbers in sorted order:")
for i in range(n):
    roll_numbers.append(int(input()))

key=int(input("Enter roll number to search: "))
result= linear_search(roll_numbers, key)

if result!=-1:
    print("Student did not attended the training program.")
    print("Position:", result + 1)

else:
    print("Student attended the training program.")