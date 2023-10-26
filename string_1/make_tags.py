def main():
    tag , word = input("Enter the values: ").split(" ")

    print(make_tags(tag, word))

def make_tags(t,w):
    return "<"+t+">"+w+"</"+t+">"

if __name__ == "__main__":
    main()