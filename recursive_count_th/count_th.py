'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #there will not be a 'th' if there are less than 2 letters
    if len(word) < 2:
        return 0
    #every two letters check if equal to 'th'
    elif word[:2] == "th":
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])

print(count_th("fresth"))
