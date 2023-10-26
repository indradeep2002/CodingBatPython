def main():
    string = input("Enter the String: ")

    print(first_two(string))

def first_two(str):
    first_two = str[:2]
    return first_two


if __name__ == "__main__":
    main()