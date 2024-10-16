import random

def give_hint(secret_word, current_hint):
    # Randomly pick an unrevealed character to reveal
    unrevealed_indices = [i for i, ch in enumerate(current_hint) if ch == '_']
    if unrevealed_indices:
        random_index = random.choice(unrevealed_indices)
        current_hint[random_index] = secret_word[random_index]
    return current_hint

def word_guessing_game(secret_word):
    secret_word = secret_word.lower()
    current_hint = ['_' if ch != ' ' else ' ' for ch in secret_word]
    attempts = 0
    
    print("Welcome to the word guessing game!")
    
    while ''.join(current_hint) != secret_word:
        print(f"\nYour hint is: {' '.join(current_hint)}")
        guess = input("What is your guess? ").lower()
        attempts += 1
        
        if guess == secret_word:
            print(f"\nCongratulations! You guessed it!")
            print(f"It took you {attempts} guesses.")
            return
        else:
            current_hint = give_hint(secret_word, current_hint)
    
    print(f"\nCongratulations! You guessed it!")
    print(f"It took you {attempts} guesses.")

# Example usage with the word 'mosiah'
word_guessing_game('book')
