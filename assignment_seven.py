def choice():
choice1 = input("press e to encode press d to decode or press q to quit:")
if choice1 == "e":
    print("encode")
elif choice1 == "d":
    print("decode")
else:
    print("Okay bye")


def main():
    if choice1 == "e":
        input("What would you like to encode?")
    elif choice1 == "d":
        input("What would you like to decode?")
number = int(input("Choose a number between 0-25"))
alphabet = "abcdefghijklmnopqrstuvwxyz"



main()