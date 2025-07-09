import sys

def main():
    if len(sys.argv) != 3:
        print("Использование: python script.py n m")
        return

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    array = list(range(1, n + 1))

    path = []

    current_index = 0

    while True:
        start_element = array[current_index]
        path.append(str(start_element))
        current_index = (current_index + m) % n
        if current_index == 0:
            break

    print("".join(path))

if __name__ == "__main__":
    main()
