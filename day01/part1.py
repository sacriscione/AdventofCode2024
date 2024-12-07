# Day 1: Historian Hysteria

def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # calculate the total distance
    total_distance = sum(abs(l - r) for 1, r in zip(left_sorted, right_sorted))

    return total_distance

# example input lists
left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 9, 3]

# calculate and print total distance
total_distance = calculate_total_distance(left_list = right_list)
print(f"Total Distance: {total_distance}")