def find_min(list):
    if len(list) == 0:
        return None
    min_value = list[0]
    for item in list:
        if item < min_value:
            min_value = item
    return min_value

if __name__ == "__main__":
    numbers = [20, 35, 1, 26, 38]
    print("Min value:", find_min(numbers)) 
    print("Min value (empty):", find_min([])) 