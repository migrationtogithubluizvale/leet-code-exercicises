# return a bool
def check_permutation(string1, string2):
    count_letters = {}
    for char in string1:
        if char in count_letters.keys():
            count_letters[char] += 1
        else:
            count_letters[char] = 1

    for char in string2:
        if char in count_letters.keys():
            count_letters[char] -= 1
        else:
            return False

        if count_letters[char] < 0:
            return False
    return True