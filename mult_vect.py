# Given two lists of numbers of the same length, create a new list by
# multiplying the pairs of numbers in corresponding positions in the two
# lists.  Example:

# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]

first_list = [2, 4, 5]
second_list = [2, 3, 6]
new_list = []
iterator = 0

first_length = len(first_list)
second_length = len(second_list)
if first_length == second_length:
    while iterator < first_length:
        new_number = first_list[iterator] * second_list[iterator]
        new_list.append(new_number)
        iterator += 1

print(f"First List: {first_list}")
print(f"Second List: {second_list}")
print(f"New List: {new_list}")