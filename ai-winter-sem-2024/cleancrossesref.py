import random

def create_environment():
    environment = [['-' for _ in range(5)] for _ in range(5)]
    for _ in range(random.randint(1, 5)):
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        environment[row][col] = 'X'
    return environment

def display_environment(environment):
    for row in environment:
        print(' '.join(row))
    print()

def clean_cross_marks(environment):
    replaced_items = 0
    for i in range(5):
        for j in range(5):
            if environment[i][j] == 'X':
                print(f"Cleaning 'X' at position ({i+1}, {j+1})")
                environment[i][j] = '-'
                replaced_items += 1
    return replaced_items

def main():
    environment = create_environment()

    print("Initial Environment:")
    display_environment(environment)

    crosses_before_cleaning = sum(row.count('X') for row in environment)
    print(f"Number of crosses before cleaning: {crosses_before_cleaning}")

    replaced_items = clean_cross_marks(environment)

    print("Final Environment after cleaning:")
    display_environment(environment)
    print(f"Number of replaced items: {replaced_items}")

if __name__ == "__main__":
    main()
