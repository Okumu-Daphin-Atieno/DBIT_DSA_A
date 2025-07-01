def sum_of_elements(list):
    total = 0
    for item in list:
        total += item
    return total

if __name__ == "__main__":
    numbers = [5, 20, 30, 22, 15]
    print("Sum of elements:", sum_of_elements(numbers))  