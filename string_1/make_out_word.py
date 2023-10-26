def main():
    out , word = input("Enter the values: ").split(" ")

    print(make_out_word(out, word))

def make_out_word(out, word):
    return out[:2]+word+out[2:]


if __name__ == "__main__":
    main()

