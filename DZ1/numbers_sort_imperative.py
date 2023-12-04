def sort_list_imperative(numbers):

    for i in range(1, len(numbers)):
        for j in range(1, len(numbers)):
            if numbers[j] < numbers[j - 1]:
                temp = numbers[j]
                numbers[j] = numbers[j - 1]
                numbers[j - 1] = temp

    return numbers
