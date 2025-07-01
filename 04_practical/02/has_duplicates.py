def has_duplicates(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return True
    return False

if __name__ == "__main__":
    print("Has duplicates:", has_duplicates([1, 2, 3, 4, 2]))  # Output: True
    print("Has duplicates:", has_duplicates([1, 2, 3, 4]))      