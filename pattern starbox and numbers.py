def print_pattern():
    for i in range(5):
        for j in range(5):
            if i == 0 or i == 4 or j == 0 or j == 4:
                print("*", end=" ")
            elif i == 1:
                print(j, end=" ")
            elif i == 2:
                print(j + 3, end=" ")
            elif i == 3:
                print(j + 6, end=" ")
        print()

# Call the function to print the pattern
print_pattern()