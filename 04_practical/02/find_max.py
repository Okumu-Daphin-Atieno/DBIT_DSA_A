def find_max(list):
    if len(list) == 0:
        return None
    max_value = list[0]
    for item in list:
        if item > max_value:
            max_value = item
    return max_value

if __name__ == "__main__":
    numbers = [20, 35, 1, 26, 38]
    print("Max value:", find_max(numbers)) 
    print("Max value (empty):", find_max([])) 