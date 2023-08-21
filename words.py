def print_upper_words(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if ((word.startswith(letter)) or (word.startswith(letter.upper()))):
                print(word.upper())
                break


print_upper_words(
    ["hello", "hey", "goodbye", "yo", "yes", "bat"], must_start_with={"h", "y"})