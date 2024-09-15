def create_new_list(list1, list2):
    newlis = []
    for i in list1:
        if i % 2 != 0:
            newlis.append(i)
    for i in list2:
        if i % 2 == 0:
            newlis.append(i)
    return newlis
# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [10, 15, 20, 25, 30]

print(create_new_list(list1, list2))