# Chad Scott
# 11/6/18
# This Program takes text that is inputted by the user and either encodes it or decodes it according to the alphabet


def choice():
    """
    This function asks the user if they would like to encode or decode or quit
    :return:
    """
    choice = input("press e to encode press d to decode or press q to quit:")
    if choice == "e":
        return "e"

    elif choice == "d":
        return "d"
    else:
        print("Okay bye")


def main():
    user_choice = choice()
    if user_choice == "e":
        number = int(input("Choose a number between 0-25:"))
        phrase = input("What would you like to encode?")
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        # This takes the letter from the alphabet and puts it in the correct position
        first = alphabet[0:number]
        last = alphabet[number:]
        final = last + first
        encoded = ""
        # This is saying to add the letter from the alphabet index
        for x in phrase:
            if x == " ":
                encoded = encoded + " "
            else:
                code = alphabet.index(x)
                final2 = final[code]
                encoded = encoded + final2
        print(encoded)
    elif user_choice == "d":
        number = int(input("Choose a number between 0-25:"))
        phrase = input("What would you like to encode?")
        alphabet = "zyxwvutsrqponmlkjihgfedcba"
        first = alphabet[0:number]
        last = alphabet[number:]
        final = last + first
        decoded = ""
        for x in phrase:
            if x == " ":
                decoded = decoded + " "
            else:
                code = alphabet.index(x)
                final2 = final[code]
                decoded = decoded + final2
        print(decoded)


main()