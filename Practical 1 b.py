def binary_search(roll_numbers, key):
    low=0
    high=len(roll_numbers)-1
    while low<=high:
        mid=(low+high) //2
        if roll_numbers[mid]==key:
            return mid
        elif roll_numbers[mid] <key:
            low=mid+1
            
        else:
            high-mid
            return -1

n=int(input("Enter number of students: "))

roll_numbers = []
print("Enter roll numbers in sorted order:")

for i in range(n):
    roll_numbers.append(int(input()))
    key=int(input("Enter roll number to search: "))
    result = binary_search(roll_numbers, key)
    if result != -1:
        print("Student attended the training program.")
        print("Position:",)
        result+1
    else:
        print("Student did not attend the training program.")