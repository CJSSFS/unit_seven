def is_paleindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


print(is_paleindrome("racecar"))
print(is_paleindrome("reverse"))
