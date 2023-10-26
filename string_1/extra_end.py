def main():
    string = input("Enter the String: ")

    print(extra_end(string))

def extra_end(str):
    n = len(str)
  
    s = str[n-2:]
    return s*3

if __name__ == "__main__":
    main()