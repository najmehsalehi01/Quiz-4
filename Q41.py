#The author's name is Julia Bub
# The sub is actually a hashtag, so we easily can work with that instead of using sub and playing with the len(sub)
# In fact the function can easily just take a string and check for the hashtags in the while loop.
def count_hashtag(string, sub):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            total += 1
            index += len(sub)
        else:
            index += 1
    return(total)

print(count_hashtag("#Halloweekend#taylorswift#hello#", "#"))
