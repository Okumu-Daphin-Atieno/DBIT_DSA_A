def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

if __name__ == "__main__":
    numbers = [10, 20, 30, 40]
    print("Index of 30:", linear_search(numbers, 30)) 
    print("Index of 50:", linear_search(numbers, 50))  