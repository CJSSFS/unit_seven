def choice():
    choice = input("press e to encode press d to decode or press q to quit:")
    if choice == "e":
        return "e"

    elif choice == "d":
        return "d"
    else:
        print("Okay bye")


def main():
    if choice == "e":
        number = int(input("Choose a number between 0-25:"))
        phrase = input("What would you like to encode?")
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        first = alphabet[0:number]
        last = alphabet[number:]
        final = last + first
        encoded = ""
        for x in phrase:
            if x == " ":
                encoded = encoded + " "
            else:
                code = alphabet.index(x)
                final2 = final[code]
                encoded = encoded + final2
        print(encoded)
    elif choice == "d":
        number = int(input("Choose a number between 0-25:"))
        phrase = input("What would you like to encode?")
        alphabet = "zyxwvutsrqponmlkjihgfedcba"
        first = alphabet[0:number]
        last = alphabet[number:]
        final = last + first
        encoded = ""
        for x in phrase:
            if x == " ":
                decoded = decoded + " "
            else:
                code = alphabet.index(x)
                final2 = final[code]
                decoded = decoded + final2
        print(decoded)


main()