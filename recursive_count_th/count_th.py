'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # if the length of word is less than 2 return 0
    # if (word - 1) is equal to "th" return 1
    # if the next 2 letters are "th" return 1 + the count of words 

    # base case
    if len(word) < 2:
        return 0
    # TBC
    elif word[0:2] == 'th':
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])
    
print(count_th("excellence"))
print(count_th("authoritarian"))
print(count_th("theeth"))
print(count_th("thethethethe")) # for a lack of a better word
