def choice():
    choice = input("press e to encode press d to decode or press q to quit:")
    if choice == "e":
        print("encode")
    elif choice == "d":
        print("decode")
    else:
        print("Okay bye")


def main():
    choice1 = int(input("Choose a number between 0-25"))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    first = alphabet[0:choice1]
    last = alphabet[choice1:]
    final = first + last
    encoded = ""
    phrase = input("What would you like to encode")
    



        # if choice == "e":
        #     input("What would you like to encode?")
        # elif choice == "d":
        #     input("What would you like to decode?"

main()