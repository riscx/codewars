# 
'''
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
'''
# So anything 5 letters or more is reversed
# only letters in words are reversed
# word placement in sentence stays same

def spin_words(sentence):
    # Split words into a list form, splits on space
    words = sentence.split(' ')
    # Need to loop through the list.
    # #numerate returns 2 variable list set.
    for wordp,word in enumerate(words):
        if len(word)>=5:
            words[wordp] = word[::-1] # awesome ::-1 on list will start at end and process in reverse
    return ' '.join(word for word in words) # join everything back together by spaces. join revering the split.

print("test: ")
print(spin_words('I like to spend lots of time solving Problems.'))
