import random

def create_env():
    env = [['-' for _ in range(5)] for _ in range(5)]
    for _ in range(random.randint(1, 5)):
        row, col = random.randint(0,4), random.randint(0,4)
        env[row][col] = 'x'
    return env

def display_env(env):
    for row in env:
        print(' '.join(row))
    print()

def clean_crosses(env):
    replaced_count = 0
    for i in range(5):
        for j in range(5):
            if env[i][j]=='x':
                env[i][j]=='-'
                replaced_count+=1
    return replaced_count

def main():
    env = create_env()
    print("Initial environment:")
    display_env(env)
    print("Number of crosses cleaned: ", clean_crosses(env))

if __name__ == "__main__":
    main()





