# Write a function that stutters a word as if someone is
# struggling to read it. The first two letters are repeated
# twice with an ellipsis ... and space after each, and 
# then the word is pronounced with a question mark ?.

# Examples

# stutter("incredible") ➞ "in... in... incredible?"

# stutter("enthusiastic") ➞ "en... en... enthusiastic?"

# stutter("outstanding") ➞ "ou... ou... outstanding?"

def stutter(word):
    x = word[:2]
    return f"{x}...{x}...{word}"
print(stutter("tito"))


def stutter(word: str) -> str:
    # Get the first two letters of the word
    first_two_letters = word[:2]
    
    # Create the stuttered version of the word
    stuttered_word = f"{first_two_letters}... {first_two_letters}... {word}?"
    
    return stuttered_word

# Examples of using the function
print(stutter("incredible"))


# The notation ((word: str) -> str) is a type hint in Python that indicates 
# the type of the input parameter and the return type of the function.
# Here's a breakdown of what it means:

# word: str indicates that the parameter word is expected to be of type str (string).
# -> str indicates that the function will return a value of type str (string).