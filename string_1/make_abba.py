def main():
    s1 , s2 = input("Enter the values: ").split(" ")

    print(make_abba(s1, s2))

def make_abba(a, b):
    return a+b+b+a

if __name__ == "__main__":
    main()

    