def secondOrderElements(arr:list[int]):
    inf = "Inf"
    neg_inf = "-Inf"

    largest = float(neg_inf)
    second_largest = float(neg_inf)

    smallest = float(inf)
    second_smallest = float(inf)

    for val in arr:
        # Check for largest
        if val > largest:
            second_largest = largest
            largest = val
        elif val > second_largest and val < largest:
            second_largest = val

        # Check for smallest
        if val <smallest:
            second_smallest = smallest
            smallest = val
        elif val <second_smallest and val > smallest:
            second_smallest = val
    
    return [second_largest, second_smallest]

arr = [1,2,3,4,5,6,7,8,9,10]
print(secondOrderElements(arr))
        