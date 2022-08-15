# should return  true or false

# this has time complexity of O(n) and space complexity of O(n)
def hasAllUniqueCharacter(string):
    dictionary_count = {}
    for char in string:
        if char in dictionary_count.keys():
            dictionary_count[char] += 1
        else:
            dictionary_count[char] = 1
    
    for v in dictionary_count.values():
        if v > 1:
            return False
    
    return True

def hasAllUniqueCharacter(string):
    new_string = ''
    cc = 0
    while cc < len(string):
        
        if string[cc] in new_string:
            return False

        new_string += string[cc]

        cc += 1
    
    return True