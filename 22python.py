def count_occurrences(lst, target):
    count = 0
    for element in lst:
        if element == target:
            count += 1
    return count

my_list = [1, 2, 3, 4, 2, 2, 5, 2]
target_element = 2
result = count_occurrences(my_list, target_element)
print(f"The element {target_element} appears {result} times in the list.")
