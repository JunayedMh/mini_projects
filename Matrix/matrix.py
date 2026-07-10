import random
import time
import os

CHARACTERS = ["0", "1", "X", "Y", "Z", "$", "#", "@", "%", "@", "+", "*"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    width = 160

    print("\033[1;32m")
    print("Press CTRL + C to stop Matrix...")
    time.sleep(2)

    try:
        while True:
            row = ""
            for _ in range(width):
                if random.random() < 0.20:
                    row += random.choice(CHARACTERS)
                else:
                    row += " "
            print(row)
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\033[0m\nMatrix execution stopped safely.")

if __name__ == "__main__":
    main()