word="Alphabet"
attempt=len(word)+4
wordDisplay=['_' for _ in word]
print("Welcome to Name guesser")
while attempt>=0 and '_' in wordDisplay:
    print('\n'+' '.join(wordDisplay))
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for index,letter in enumerate(word):
            if guess== letter:
                wordDisplay[index]=guess
    else:
        print("Oops... The letter is not in the word")
        attempt-=1

if '_' not in wordDisplay:
    print("You got it coorect. The word is ", word)
else:
    print("You are out of attempts... The correct word was: ",word)