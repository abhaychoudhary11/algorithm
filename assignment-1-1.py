def bubble_sort(empid, salary):
    n = len(empid)
    swaps = 0
    comparisons = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            comparisons += 1
            if salary[j] < salary[j + 1] or (salary[j] == salary[j + 1] and empid[j] < empid[j + 1]):
                salary[j], salary[j + 1] = salary[j + 1], salary[j]
                empid[j], empid[j + 1] = empid[j + 1], empid[j]
                swaps += 1
    return swaps, comparisons

def selection_sort(empid, salary):
    n = len(empid)
    swaps = 0
    comparisons = 0
    for i in range(n - 1):
        maxindex = i
        for j in range(i + 1, n):
            comparisons += 1
            if salary[j] > salary[maxindex] or (salary[j] == salary[maxindex] and empid[j] > empid[maxindex]):
                maxindex = j
        if maxindex != i:
            salary[i], salary[maxindex] = salary[maxindex], salary[i]
            empid[i], empid[maxindex] = empid[maxindex], empid[i]
            swaps += 1
    return swaps, comparisons

def shell_sort(empid, salary):
    n = len(empid)
    swaps = 0
    comparisons = 0
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp_salary = salary[i]
            temp_empid = empid[i]
            j = i
            while j >= gap and (salary[j - gap] < temp_salary or \
                                (salary[j - gap] == temp_salary and empid[j - gap] < temp_empid)):
                comparisons += 1
                salary[j] = salary[j - gap]
                empid[j] = empid[j - gap]
                j -= gap
                swaps += 1
            salary[j] = temp_salary
            empid[j] = temp_empid
        gap //= 2
    return swaps, comparisons

if __name__ == "__main__":
    empid = [1, 3, 8, 5, 8]
    salary = [100, 800, 400, 800, 700]

    empid1, salary1 = empid[:], salary[:]
    empid2, salary2 = empid[:], salary[:]
    empid3, salary3 = empid[:], salary[:]

    swaps, comparisons = bubble_sort(empid1, salary1)
    print("BUBBLE SORT OUTPUT--> ", empid1)
    print("NUMBER OF SWAPS IN BUBBLE SORT --> ", swaps)
    print("NUMBER OF COMPARISONS IN BUBBLE SORT --> ", comparisons)

    swaps, comparisons = selection_sort(empid2, salary2)
    print("SELECTION SORT OUTPUT --> ", empid2)
    print("NUMBER OF SWAPS IN SELECTION SORT --> ", swaps)
    print("NUMBER OF COMPARISONS IN SELECTION SORT --> ", comparisons)

    swaps, comparisons = shell_sort(empid3, salary3)
    print("SHELL SORT OUTPUT --> ", empid3)
    print("NUMBER OF SWAPS IN SHELL SORT --> ", swaps)
    print("NUMBER OF COMPARISONS IN SHELL SORT --> ", comparisons)