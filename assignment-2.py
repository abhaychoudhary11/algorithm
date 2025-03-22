def linear_search(students):
    result = []
    iteration1 = 0
    for student in students:
        iteration1 += 1
        if student["height"] > 5.0:
            result.append(student)
    return result, iteration1

def binary_search(students):
    result = []
    iteration2=0
    left, right = 0, len(students) - 1

    while left <= right:
        iteration2 += 1
        mid = (left + right) // 2
        if students[mid]["height"] > 5.0:
            result.extend(students[mid:])
            right = mid - 1
        else:
            left = mid + 1

    return result, iteration2

def main():
    students = []

    n = int(input("Enter the number of students: "))
    for _ in range(n):
        name = str(input("Enter the student's name: "))
        height = float(input(f"Enter the height of {name} in feet: "))
        students.append({"name": name, "height": height})

    linear_results, iteration1 = linear_search(students)
    print("\nLinear Search Results:")
    for student in linear_results:
        print(f"Name: {student['name']}, Height: {student['height']}")

    print(f"Total iterations in Linear Search: {iteration1}")

    students_sorted = sorted(students, key=lambda x: x["height"])

    binary_results, iteration2 = binary_search(students_sorted)
    print("\nBinary Search Results:")
    for student in binary_results:
        print(f"Name: {student['name']}, Height: {student['height']}")
        
    print(f"Total iterations in Binary Search: {iteration2}")

if __name__ == "__main__":
    main()
