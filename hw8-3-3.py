# Ryan Lugo: RJL 12/9/21

def three_letter_words(lst):

    letter_words = 0
    looped = 0

    while looped < len(lst):
        if len(lst[looped]) == 3:
            letter_words += 1
        looped += 1
    return letter_words

print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)